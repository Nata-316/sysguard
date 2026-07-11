import smtplib
import os
from dotenv import load_dotenv

from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).parent.parent / '.env')

def send_alert(subject, body):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")
    
    message = f"Subject: {subject}\n\n{body}"
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    server.quit()

if __name__ == "__main__":
    send_alert("SysGuard Test", "This is a test alert from SysGuard")