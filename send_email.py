import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv  

PORT = 587  
EMAIL_SERVER = "smtp-mail.outlook.com"  

current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)


sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")


def send_email(subject, receiver_email, name):

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("DS PBL", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi {name},
        This is a test.
        
        """
    )

    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Hi {name},</p>
        <p>This is a test.</p>
        
      </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    send_email(
        subject="This is a test",
        name="Rameez Shaikh",
        receiver_email="shaikhrameez516@gmail.com",
        
    )