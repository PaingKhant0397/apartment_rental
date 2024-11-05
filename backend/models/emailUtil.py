import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()  # Ensure .env is loaded at the start
SMTP_PW = os.getenv('SMTP_PW')


class EmailUtil:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.port = 587
        self.username = "paingkhant0397@gmail.com"
        self.password = SMTP_PW

    def send_email(self, subject: str, body: str, to_emails: List[str], html_body: str = None, from_email: str = None):
        from_email = from_email or self.username
        try:
            # Create the email message
            msg = MIMEMultipart('alternative')
            msg['From'] = from_email
            msg['To'] = ', '.join(to_emails)
            msg['Subject'] = subject

            # Attach the plain text and HTML versions of the email body
            msg.attach(MIMEText(body, 'plain'))  # Plain text version
            if html_body:  # Check if there's an HTML body to attach
                msg.attach(MIMEText(html_body, 'html'))  # HTML version

            # Establish a secure session with the server
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Secure the connection
                server.login(self.username, self.password)

                # Send the email
                server.sendmail(from_email, to_emails, msg.as_string())

            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")


# Example usage
if __name__ == "__main__":
    email_util = EmailUtil()

    plain_text_body = "This is a plain text email."
    html_body = """\
    <html>
      <body>
        <h1>This is an HTML email</h1>
        <p style="color:blue;">This email contains <strong>HTML</strong> content.</p>
      </body>
    </html>
    """

    email_util.send_email(
        subject="Test Email with HTML",
        body=plain_text_body,
        html_body=html_body,
        to_emails=["paingphyoaungkhant@gmail.com"]
    )
