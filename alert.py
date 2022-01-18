import smtplib
from email.message import EmailMessage

import json
import os

f = open('config.json')
data = json.load(f)

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to
    msg["from"] = "Sender Email Address"
    #Name of User is the name of the sender that you want to display

    user = data["email"]
    password = data["password"]
    #user is the email address you are using to send the email
    #password is the autogenerated password given by Google

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(user, password)
    server.send_message(msg)
    server.quit()
    f.close()
for i in range(10):
    if __name__ == "__main__":
        email_alert("Subject of Email", "Body of Email", "Reciever Email Address")


