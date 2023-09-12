import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifymee.settings')
django.setup()
from productdetail.models import productdetails
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from bs4 import  BeautifulSoup
import requests,time,smtplib
from datetime import datetime
from threading import Timer

headers = { 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# set_price = 1400

def check_price(url,dp,email,id):
    if url.count("flipkart"):
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(class_='B_NuCI').get_text()
        # print(title)
        product_title = str(title)
        product_title = product_title.strip()
        print(product_title)
        price = soup.find(class_='_30jeq3 _16Jk6d').get_text()
        # print(price)
        product_price = ''
        for letters in price:
            if letters.isnumeric() or letters == '.':
                product_price += letters
        print(float(product_price))
        if float(product_price) <= dp:
            smtpfunction()
            print('sent')
            return
        else:
            print('not sent')
        Timer(60, check_price).start()
    else:
        print("Not flipkart")


def smtpfunction():
    print("Raveena")
    import smtplib
    EMAIL_ADDRESS = "raveenapatidar953@gmail.com"
    EMAIL_PASSWORD = "hxndzixgcspsmlep"

    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

        subject = "Grab dinner this weekend"
        body = "How about dinner at 6pm this Saturday"

        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS,"patidarraveena953@gmail.com",msg)


# smtpfunction()

def fun(name):
    print(name)

def mainn():
    while(True):
        l=productdetails.objects.all()
        for i in l:
            fun(i.name)
            check_price(i.url,i.price,i.email,i.userid)
        time.sleep(60)
        break