import smtplib
from email.mime.text import MIMEText
from credentials import my_email, my_pasword

def send_mail(item, email_to = "thomasvanneuville93@gmail.com"):
    """Send automatic mails trought smtp"""
    email = my_email
    password = my_pasword
    subject = 'Warframe Alert'
    msg = MIMEText("{} in alert now!".format(item))

    msg['Subject'] = 'Warframe Alert'
    msg['From'] = email
    msg['To'] = email_to

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.starttls()
    mail.login(email, password)
    mail.send_message(msg)
    mail.close()
