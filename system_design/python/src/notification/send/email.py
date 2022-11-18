import smtplib, os, json
from email.message import EmailMessage


def notification(message):
    """
    # try:
    message = json.loads(message)
    mp3_fid = message["mp3_fid"]
    sender_address = os.environ.get("GMAIL_ADDRESS")
    sender_password = os.environ.get("GMAIL_PASSWORD")
    receiver_address = message["username"]

    msg = EmailMessage()
    msg.set_content(f"mp3 file_id: {mp3_fid} is now ready!")
    msg["Subject"] = "MP3 Download"
    msg["From"] = sender_address
    msg["To"] = receiver_address

    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.starttls()
    session.login(sender_address, sender_password)
    session.send_message(msg, sender_address, receiver_address)
    session.quit()
    """
    message = json.loads(message)
    mp3_fid = message["mp3_fid"]

    user = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASSWORD")
    smtp_server = os.environ.get("SMTP_SERVER")
    smtp_port = int(os.environ.get("SMTP_PORT"))
    sender = os.environ.get("SENDER")
    receiver = message["username"]

    message = f"""\
    Subject: "MP3 Download"
    To: {receiver}
    From: {sender}

    mp3 file_id: {mp3_fid} is now ready!"""

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(user, password)
        server.sendmail(sender, receiver, message)
    
    print("Mail Sent")


# except Exception as err:
# print(err)
# return err