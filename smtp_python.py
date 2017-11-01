#!/usr/bin/python3
__author__ = 'Kanishk Sharan'


import smtplib
from email.mime.text import MIMEText

#  ehlo foo.com
#  mail from:  foo@foo.com
#  rcpt to:  me@me.com
#  data

s = smtplib.SMTP("172.30.42.127", 25)
#s.login("user", "password")

try:
#  could use the following for a MIME message
#    f = open("myfile", "r")
#    m = MIMEText(f.read())
#    f.close()
#    m['To'] = "kesha@comegetme.com"
#    m['From'] = "kesha@gmail.com"
#    m['Subject'] = "This is a message to you"

    m = "\nThis is a message from the last session"
    s.sendmail("kanishksharan21@gmail.com", "ks223@uw.edu", m)
    #  send the MIME message
    # s.send_message(m)
    print("Finished sending message")
except Exception as e:
    print("Unable to send message: ", e)

s.quit()
