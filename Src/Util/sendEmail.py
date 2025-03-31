import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random, string
from typing import LiteralString


def generate6CharacterToken() -> LiteralString:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def sendTokenEmail(email : str, code : LiteralString) -> None:
    senderEmail = "airventure027@gmail.com"
    sendPassword = "ndxm zgqo vany mvcv"
    smtpServer = "smtp.gmail.com"     # Change to your email provider's SMTP server
    smtpPort = 587                   # SMTP port for TLS
    token = code
    subject = "✈️ Your AirVenture Password Reset Code is Here!"
    with open("Src/Util/emailResetCode.html", "r", encoding = "utf-8") as file:
        html_content = file.read()
    html_content = html_content.format(token = token)

    try:
        # Set up the email
        message = MIMEMultipart("alternative")
        message["From"] = senderEmail
        message["To"] = email
        message["Subject"] = subject

        # Attach the HTML content
        message.attach(MIMEText(html_content, "html"))

        # Connect to SMTP server and send email
        with smtplib.SMTP(smtpServer, smtpPort) as server:
            server.starttls()  # Enable security
            server.login(senderEmail, sendPassword)
            server.sendmail(senderEmail, email, message.as_string())
            print(f"Email sent successfully to {email} with token: {token}")
    except Exception as e:
        print(f"Failed to send email: {e}")





