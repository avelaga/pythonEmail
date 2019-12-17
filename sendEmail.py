import smtplib

import myconfig


def send_email(subject, msg):
    try:
        print("starting try")
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        print("about to login")
        server.login(myconfig.EMAIL_ADDRESS, myconfig.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        print("about to send email")
        server.sendmail(myconfig.EMAIL_ADDRESS, myconfig.RECIPIENT_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "hi mom"
msg = "did this work? i sent it with code"

send_email(subject, msg)
