import smtplib
import time
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen

def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'christmas_alerts@pythonscraping.com'
    msg['To'] = 'ryan@pythonscraping.com'

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

bsObj = BeautifulSoup(urlopen('https://isitchristmas.com/'), 'html.parser')
while(bsObj.find('a', {'id': 'answer'}).attrs['title'] == 'NO'):
    print('It is not Christmas yet.')
    time.sleep(3600)
bsObj = BeautifulSoup(urlopen('https://isitchristmas.com/'), 'html.parser')
sendMail("It's Christmas!", 'According to http://itischrismas.com, it is Christmas!')