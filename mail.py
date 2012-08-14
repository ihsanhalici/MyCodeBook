#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os



def mail(to, fromx, subject, text, gmail_user, gmail_pwd, mserver, mport):
   msg = MIMEMultipart()

   msg['From'] = fromx
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))


   mailServer = smtplib.SMTP(mserver, mport)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

