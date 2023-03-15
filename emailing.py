from key import key
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_SENDER = "Your email address"
PASSWORD = "Your Key"
RECEIVER = "Receiver Email Address"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up"
    email_message.set_content("Hey, a new customer showed up")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(EMAIL_SENDER, PASSWORD)
    gmail.sendmail(EMAIL_SENDER, RECEIVER, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email("images/1.png")