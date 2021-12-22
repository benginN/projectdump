#Don't forget to import the things below and change 'GMAIL' and 'PASSWORD'as yours. The mail that logged in must have "Less Secure Apps" allowed.

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
msg['From'] = 'orhan123321bengin@gmail.com'
msg['To'] = 'orhan123321bengin@gmail.com'
msg['Subject'] = 'Your Verification Code'
message = "Your Verification Code Is: " + facode
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('GMAIL', 'PASSWORD')
mailserver.sendmail('orhan123321bengin@gmail.com','orhan123321bengin@gmail.com',msg.as_string())
mailserver.quit()

while True:
 facodetry = input("G-Mailinize Gelen 2 Faktörlü Doğrulama Kodunu Giriniz: ")
 if facodetry == facode:
    print ("You Have Succesfully Logged In.")
    break
    
 else:
  print("Wrong Verification Code, Please Try Again.")
