import json
import os
import re
import smtplib
from email.message import EmailMessage
from email.utils import parseaddr
from http.server import BaseHTTPRequestHandler


MAX_BODY_BYTES = 16_000
MAX_FIELD_LENGTHS = {"name": 120, "email": 254, "interest": 160, "message": 5000}
EMAIL_PATTERN = re.compile(r"[^\s@]+@[^\s@]+\.[^\s@]+")


def send_json(handler, status, payload):
    body = json.dumps(payload).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Cache-Control", "no-store")
    handler.send_header("X-Content-Type-Options", "nosniff")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # A lightweight diagnostic response; never expose credentials or config.
        if self.path.split("?", 1)[0] == "/api/contact":
            send_json(self, 405, {"ok": False, "error": "Use POST to send an enquiry."})
        else:
            send_json(self, 404, {"ok": False, "error": "Not found."})

    def do_POST(self):
        if self.path.split("?", 1)[0] != "/api/contact":
            send_json(self, 404, {"ok": False, "error": "Not found."})
            return

        content_type = self.headers.get("Content-Type", "")
        if "application/json" not in content_type.lower():
            send_json(self, 415, {"ok": False, "error": "Send the form as JSON."})
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
        except (TypeError, ValueError):
            length = 0
        if length <= 0:
            send_json(self, 400, {"ok": False, "error": "The enquiry is empty."})
            return
        if length > MAX_BODY_BYTES:
            send_json(self, 413, {"ok": False, "error": "The enquiry is too large."})
            return

        try:
            data = json.loads(self.rfile.read(length).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            send_json(self, 400, {"ok": False, "error": "Invalid form data."})
            return

        if not isinstance(data, dict):
            send_json(self, 400, {"ok": False, "error": "Invalid form data."})
            return

        # Honeypot: return success to bots without sending mail.
        if str(data.get("website", "")).strip():
            send_json(self, 200, {"ok": True, "message": "Enquiry received."})
            return

        values = {}
        for key, max_length in MAX_FIELD_LENGTHS.items():
            value = data.get(key, "")
            if not isinstance(value, str):
                send_json(self, 400, {"ok": False, "error": "Please check the form fields."})
                return
            value = value.strip()
            if len(value) > max_length:
                send_json(self, 400, {"ok": False, "error": "One of the fields is too long."})
                return
            values[key] = value

        name = values["name"]
        email = values["email"]
        interest = values["interest"]
        message = values["message"]
        _, parsed_email = parseaddr(email)

        if (
            not name
            or not email
            or not interest
            or parsed_email != email
            or not EMAIL_PATTERN.fullmatch(email)
        ):
            send_json(self, 400, {"ok": False, "error": "Enter your name and a valid email address."})
            return

        # Gmail works with an App Password when 2-Step Verification is enabled.
        # All credentials belong in Vercel Environment Variables, never in source code.
        smtp_host = os.environ.get("SMTP_HOST", "smtp.gmail.com").strip()
        try:
            smtp_port = int(os.environ.get("SMTP_PORT", "465"))
        except ValueError:
            send_json(self, 503, {"ok": False, "error": "Email delivery is misconfigured. Please try again later."})
            return

        smtp_user = os.environ.get("SMTP_USER", "").strip()
        smtp_password = os.environ.get("SMTP_PASSWORD", "")
        contact_to = os.environ.get("CONTACT_TO", "suryalh44@gmail.com").strip()

        if not all((smtp_host, smtp_user, smtp_password, contact_to)):
            send_json(self, 503, {"ok": False, "error": "Email delivery is not configured yet. Please try again later."})
            return
        if smtp_port not in (465, 587):
            send_json(self, 503, {"ok": False, "error": "Use SMTP port 465 or 587 in the email settings."})
            return

        safe_interest = interest.replace("\r", " ").replace("\n", " ")[:160]
        mail = EmailMessage()
        mail["Subject"] = f"Kreovant website enquiry: {safe_interest}"
        mail["From"] = smtp_user
        mail["To"] = contact_to
        mail["Reply-To"] = email
        mail.set_content(
            "A new enquiry was submitted through the Kreovant website.\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Interest: {interest}\n\n"
            f"Message:\n{message or '(No message provided)'}\n"
        )

        try:
            if smtp_port == 465:
                with smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=15) as server:
                    server.login(smtp_user, smtp_password)
                    server.send_message(mail)
            else:
                with smtplib.SMTP(smtp_host, smtp_port, timeout=15) as server:
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(smtp_user, smtp_password)
                    server.send_message(mail)
        except (smtplib.SMTPException, OSError, TimeoutError):
            # Keep provider details out of public responses; inspect Vercel Function Logs.
            send_json(self, 502, {"ok": False, "error": "Email could not be sent. Check the mail settings and try again."})
            return

        send_json(self, 200, {"ok": True, "message": "Thanks, your enquiry has been sent. We'll be in touch."})
