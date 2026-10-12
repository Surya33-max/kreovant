import json
import os
import re
import smtplib
from email.message import EmailMessage
from email.utils import parseaddr

from http.server import BaseHTTPRequestHandler


MAX_BODY_BYTES = 16_000
MAX_FIELD_LENGTHS = {"name": 120, "email": 254, "interest": 160, "message": 5000}


def response(handler, status, payload):
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
        response(self, 405, {"ok": False, "error": "Use POST to send an enquiry."})

    def do_POST(self):
        if self.path.split("?", 1)[0] != "/api/contact":
            response(self, 404, {"ok": False, "error": "Not found."})
            return

        content_type = self.headers.get("Content-Type", "")
        if "application/json" not in content_type.lower():
            response(self, 415, {"ok": False, "error": "Send the form as JSON."})
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            length = 0
        if length <= 0 or length > MAX_BODY_BYTES:
            response(self, 413, {"ok": False, "error": "The enquiry is empty or too large."})
            return

        try:
            raw = self.rfile.read(length)
            data = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            response(self, 400, {"ok": False, "error": "Invalid form data."})
            return

        if not isinstance(data, dict):
            response(self, 400, {"ok": False, "error": "Invalid form data."})
            return

        # Honeypot field: quietly accept bot submissions without sending mail.
        if str(data.get("website", "")).strip():
            response(self, 200, {"ok": True, "message": "Enquiry received."})
            return

        values = {}
        for key, max_length in MAX_FIELD_LENGTHS.items():
            value = data.get(key, "")
            if not isinstance(value, str):
                response(self, 400, {"ok": False, "error": "Please check the form fields."})
                return
            value = value.strip()
            if len(value) > max_length:
                response(self, 400, {"ok": False, "error": "One of the fields is too long."})
                return
            values[key] = value

        name = values["name"]
        email = values["email"]
        interest = values["interest"]
        message = values["message"]

        parsed_name, parsed_email = parseaddr(email)
        if not name or not email or not interest or parsed_email != email or not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
            response(self, 400, {"ok": False, "error": "Enter your name and a valid email address."})
            return

        smtp_host = os.environ.get("SMTP_HOST", "").strip()
        smtp_port = int(os.environ.get("SMTP_PORT", "465"))
        smtp_user = os.environ.get("SMTP_USER", "").strip()
        smtp_password = os.environ.get("SMTP_PASSWORD", "")
        contact_to = os.environ.get("CONTACT_TO", "suryalh44@gmail.com").strip()

        if not all((smtp_host, smtp_user, smtp_password, contact_to)):
            response(self, 503, {"ok": False, "error": "Email delivery is not configured yet. Please try again later."})
            return

        subject = "Kreovant enquiry: " + interest.replace("\r", " ").replace("\n", " ")[:160]
        mail = EmailMessage()
        mail["Subject"] = subject
        mail["From"] = smtp_user
        mail["To"] = contact_to
        mail["Reply-To"] = email
        mail.set_content(
            "A new enquiry was sent through the Kreovant website.\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Interest: {interest}\n\n"
            f"Message:\n{message or '(No message provided)'}\n"
        )

        try:
            if smtp_port == 465:
                with smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=12) as server:
                    server.login(smtp_user, smtp_password)
                    server.send_message(mail)
            else:
                with smtplib.SMTP(smtp_host, smtp_port, timeout=12) as server:
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(smtp_user, smtp_password)
                    server.send_message(mail)
        except (smtplib.SMTPException, OSError, TimeoutError):
            response(self, 502, {"ok": False, "error": "The email could not be sent right now. Please try again shortly."})
            return

        response(self, 200, {"ok": True, "message": "Thanks, your enquiry has been sent. We'll be in touch."})
