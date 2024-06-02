import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from datetime import datetime
import pytz

class SendWelcomMail():
    def __init__(self,RECEIVER_MAIL,):
        self.send_email(RECEIVER_MAIL)

    def send_email(self,RECEIVER_MAIL):
        sender_email = 'rikenkhadela777@gmail.com'
        sender_password = 'hfac mvld ecjx clru'
        receiver_email = RECEIVER_MAIL

        # Get current time in IST timezone
        # ist = pytz.timezone('Asia/Kolkata')  # IST timezone
        # current_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')

        # Include date and time in the email body
        body = '''
                Dear User,

                We are thrilled to welcome you to IGsolar notifications! Thank you for subscribing and choosing to stay updated with our latest news, events, and exclusive offers.
                With this subscription, you'll receive:

                - Timely updates on new content
                - Exclusive promotions and discounts
                - Important announcements and events

                Your engagement and support mean a lot to us. Feel free to reach out to us at any time with feedback or questions.

                Once again, thank you for subscribing and becoming a part of our community!

                "Thank you for subscribing!"

                Best regards,
                IGsolar.
                '''

        message = MIMEText(body)
        message["Subject"] = 'Welcome to IGsolar Notifications!'
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Date"] = formatdate(localtime=True)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())