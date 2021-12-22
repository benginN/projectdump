#Don't forget to import the things below and change 'GMAIFROM', GMA and 'PASSWORD'as yours. The mail that logged in must have "Less Secure Apps" allowed. 

import random
import requests
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import string


randomised= random.randint(1,999999)  
facode= (str(int(randomised)))


msg = MIMEMultipart()
msg['From'] = 'GMAILFROM'
msg['To'] = 'GMAILTO'
msg['Subject'] = 'Your Verification Code'
message = "Your Verification Code Is: " + facode
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('GMAILFROM', 'PASSWORD')
mailserver.sendmail('GMAILFROM','GMAILTO',msg.as_string())
mailserver.quit()

while True:
 facodetry = input("Enter the Verification Code That Has Been Sent To Your Mailbox: ")
 if facodetry == facode:
    print ("You Have Succesfully Logged In.")
    break
    
 else:
  print("Wrong Verification Code, Please Try Again.")
