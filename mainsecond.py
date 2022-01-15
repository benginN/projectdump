import requests
from bs4 import *
import time
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


while True:
    url= ["http://127.0.0.1:5500/HTML+CSS+JS/deneme.html", "http://127.0.0.1:5500/HTML+CSS+JS/Calculator.html", "http://127.0.0.1:5500/HTML+CSS+JS/asd.html"]
    x = 0

    while x < len(url):
        def sendMail():
            msg = MIMEMultipart()
            msg['From'] = 'ayakkabinotify@gmail.com'
            msg['To'] = 'ayakkabinotify@gmail.com'
            msg['Subject'] = 'Web Monitoring'
            message = str(url[x]) + " Has Been Changed"
            msg.attach(MIMEText(message))
            mailserver = smtplib.SMTP('smtp.gmail.com',587)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login('ayakkabinotify@gmail.com', 'dFeS-3XdK-2HgDs')
            mailserver.sendmail('ayakkabinotify@gmail.com','ayakkabinotify@gmail.com',msg.as_string())
            mailserver.quit()


        firstRequests = requests.get(url[x])
        firstBeautify = BeautifulSoup(firstRequests.content, 'html.parser')
        firstHTML = firstBeautify.find('html')
        print(str((x)+ 1) + "." + "Html Taken")

        time.sleep(4)

        lastRequests = requests.get(url[x])
        lastBeautify = BeautifulSoup(lastRequests.content, 'html.parser')
        lastHTML = lastBeautify.find('html')

        if lastHTML == firstHTML:
            print('Same')

        elif lastHTML != firstHTML:
            print("Different")
            sendMail()
        
        x = x + 1