import smtplib
from email.message import EmailMessage

def Alert(subject, to, body):
    message = EmailMessage()
    message.addContent(body)
    message["subject"] = subject
    message["to"] = to
    
    user = "test1@gmail.com"
    password = "123456"
    message["from"] = user
     
    mail = smtplib.SMTP("test2@gmail.com", 587)
    mail.starttls()
    mail.login(user, password)
    mail.send_message(message)
    
    mail.quit()
    
if __name__ == "__main__":
    Alert("Hello World :))")