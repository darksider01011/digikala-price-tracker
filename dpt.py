import sys
import os
import time
import argparse
import warnings
import sqlite3
import smtplib
import requests
from unidecode import unidecode
from datetime import datetime
from email.mime.text import MIMEText
from playwright.sync_api import sync_playwright
from email.mime.multipart import MIMEMultipart

# Configure SMTP Profile
from_address = "" #Sender Email Address EX: abcd@gmail.com
to_address = "" #Receiver Email Address EX: efgh@gmail.com
username = '' #Username(sender email address) EX: abcd@gmail.com
password = '' #Gmail App Password EX: aswd dedw frfr frgt

# Ignore Warnings
warnings.filterwarnings("ignore")

# Define Arguments
parser = argparse.ArgumentParser(description= 'Digikala Price Tracker', prog= 'dpt.py')
parser.add_argument('--dkp', type=str, help= 'Set Digikala Product ID', metavar= 'dkp-14563541', required=True)
parser.add_argument('--delay', type=str, help='Set Delay(in minutes)', metavar= '5', required=True)
parser.add_argument('--count', type=int, help='Set Counter(how many time to scrape)', metavar= '10', required=True)
parser.add_argument('--xpath', type=str, help='Set Xpath for price', default=1)

args = parser.parse_args()

dkp = args.dkp
delay = args.delay
count = args.count
xpath = args.xpath

# Minutes to Seconds
minutes = int(delay) * 60

# Linux Folder Creation
if sys.platform == "linux":

   dir = os.getcwd()
   dirr = dir + "/database"
   dirrr = dirr + "/" + dkp
   dirrrr = dirrr + "/" + dkp + ".db"

   if not os.path.exists(dirr):
      os.makedirs(dirr)

   if not os.path.exists(dirrr):
      os.makedirs(dirrr)

   if os.path.exists(dirrrr):
      os.remove(dirrrr)

   if not os.path.exists(dirrrr):
      with open(dirrrr, 'w') as fp:
          pass
   
   print("\ndpt.py is running...")

# Windows Folder Creation
if sys.platform == "win32":
    dir = os.getcwd()
    dirr = dir +"\\"+ "database\\" + dkp
    dirrr = dirr + "\\" + dkp + ".png"
    dirrrr = dirr + "\\" + dkp + ".db"

    if not os.path.exists(dirr):
       os.makedirs(dirr)

    if os.path.exists(dirrrr):
      os.remove(dirrrr)

    if not os.path.exists(dirrrr):
       with open(dirrrr, 'w') as fp:
            pass
       
    print("\ndpt.py is running...")

# Product Url
url = "https://www.digikala.com/product/" + dkp

msg = MIMEMultipart('alternative')
msg['Subject'] = "Digikala Price Tracker"
msg['From'] = from_address
msg['To'] = to_address
html = """ <!DOCTYPE html>
<html>
    <head></head>
    <body>
    <h1>{dkp}</h1>
    <br>
    <h2>Options</h2>
    <p>Count: {count}</p>
    <p>Delay: {delay} Minutes</p>
    <h2>Product</h2>
    <p>Url: {url}</p>
    </body>
</html>""".format(dkp=dkp, url=url, count=count, delay=delay)

part1 = MIMEText(html, 'html')
msg.attach(part1)
server = smtplib.SMTP('smtp.gmail.com', 587)
time.sleep(2)
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(from_address, to_address, msg.as_string())
server.quit()

# Main For Loop
for i in range(0, count):
    i += 1
    m = i - 1
    connection = sqlite3.connect(dirrrr)
    cursor = connection.cursor()
    # Sqlite Table Creation 
    cursor.execute("CREATE TABLE IF NOT EXISTS product (id INTEGER, name TEXT,dkp TEXT,date  TEXT, price INTEGER)")
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        now = datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(90000)

        if xpath != 1:
            price_a = page.locator('xpath=' + xpath)
            price_b = unidecode(price_a.text_content())
            price_c = price_b.replace(",", "")
            price_main = int(price_c)
            
            try:
                a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]/div/h1')
                product_name = a.text_content()
            except:
                product_name = "None"

            if product_name == "None":
                aa = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/h1')
                product_name = aa.text_content()

            if not os.path.exists(dirrr):
                page.screenshot(path=dirrr)
            
            page.close()
                
        else:
            
            # Xpath Number 1
            try:
                price_a = page.locator('xpath=//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[2]/div[2]/div[2]/span')
                price_b = unidecode(price_a.text_content())
                price_c = price_b.replace(",", "")
                price_one = int(price_c)
            except:
                price_one = 9999999999

            # Xpath Number 2
            try:
                price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div/div[4]/div/div/div/div[1]/div/div[2]/span')
                price_b = unidecode(price_a.text_content())
                price_c = price_b.replace(",", "")
                price_two = int(price_c)
            except:
                price_two = 9999999999

            # Xpath Number 3
            try:
                price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div/div[4]/div/div/div/div[1]/div[2]/div[1]/span')
                price_b = unidecode(price_a.text_content())
                price_c = price_b.replace(",", "")
                price_three = int(price_c)
            except:
                price_three = 9999999999

            # Xpath Number 4
            try:
                price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[1]/div[2]/div[1]/span')
                price_b = unidecode(price_a.text_content())
                price_c = price_b.replace(",", "")
                price_four = int(price_c)
            except:
                price_four = 9999999999

            # Xpath Number 5
            try:
                price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[2]/div[2]/div[1]/span')
                price_b = unidecode(price_a.text_content())
                price_c = price_b.replace(",", "")
                price_five = int(price_c)
            except:
                price_five = 9999999999

            # Xpath Number 6
            try:
                price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div/div[4]/div/div/div/div[1]/div[2]/div[2]/span')
                price_b = unidecode(price_a.text_content())
                price_c = price_b.replace(",", "")
                price_six = int(price_c)
            except:
                price_six = 9999999999

            # Xpath Number 7
            try:
                price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[2]/div/div[2]/span')
                price_b = unidecode(price_a.text_content())
                price_c = price_b.replace(",", "")
                price_seven = int(price_c)
            except:
                price_seven = 9999999999

            # Xpath Number 8
            try:
                price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[1]/div/div[2]/span')
                price_b = unidecode(price_a.text_content())
                price_c = price_b.replace(",", "")
                price_eight = int(price_c)
            except:
                price_eight = 9999999999

            # Xpath Number 9
            try:
                price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[3]/div[5]/div/div[4]/div/div/div/div[1]/div/div[1]/span')
                price_b = unidecode(price_a.text_content())
                price_c = price_b.replace(",", "")
                price_ten = int(price_c)
            except:
                price_ten = 9999999999

            # Xpath Number 10
            try:
                price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[1]/div/div[1]/span')
                price_b = unidecode(price_a.text_content())
                price_c = price_b.replace(",", "")
                price_ell = int(price_c)
            except:
                price_ell = 9999999999

            # Xpath Number 11
            try:
                price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div/div[4]/div/div/div/div[1]/div/div[1]/span')
                price_b = unidecode(price_a.text_content())
                price_c = price_b.replace(",", "")
                price_tww = int(price_c)
            except:
                price_tww = 9999999999

            # Xpath Number 12
            try:
                price_a= page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div/div[4]/div/div/div/div[2]/div[2]/div[1]/span')
                price_b = unidecode(price_a.text_content())
                price_c = price_b.replace(",", "")
                price_thh = int(price_c)
            except:
                price_thh = 9999999999
            
            # Xpath Number 13
            try:
                price_a= page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[1]/div[2]/div[2]/span')
                price_b = unidecode(price_a.text_content())
                price_c = price_b.replace(",", "")
                price_ff = int(price_c)
            except:
                price_ff = 9999999999

            # Xpath Product Name 
            try:
                a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]/div/h1')
                product_name = a.text_content()
            except:
                product_name = "None"

            if product_name == "None":
                aa = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/h1')
                product_name = aa.text_content()

            if not os.path.exists(dirrr):
                page.screenshot(path=dirrr)

            page.close()

            price_list = [price_one, price_two, price_three, price_four, price_five, price_six, price_seven, price_eight, price_ten, price_ell, price_tww, price_thh, price_ff]
            price_main = min(price_list)

        # Insert Query
        insert_query = """INSERT INTO product(id, name, dkp, date, price) VALUES (?, ?, ?, ?, ?);"""
        data_query = (i, product_name, dkp, date, price_main)
        cursor.execute(insert_query, data_query)
        connection.commit()

        # Retrieve Query
        cursor.execute("SELECT price FROM product WHERE id = '%s'" % i)
        records = cursor.fetchall()
        rec = str(records)
        price_a = rec.replace("[", "").replace("(", "").replace(",", "").replace(")", "").replace("]", "")
        next_price = int(price_a)

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Digikala Price Tracker"
        msg['From'] = from_address
        msg['To'] = to_address
        
        html = """ <!DOCTYPE html>
        <html>
        <head></head>
        <body>
        <h1>{dkp}</h1>
	    <h2>{product_name}</h2>
        <p>Price: {next_price}</p>
        <p>Time: {date}</p>
        <p>Counter: {i}</p>
        <p>Url: {url}</p>
        </body>
        </html>""".format(dkp=dkp, next_price=next_price, date=date, i=i, product_name=product_name, url=url)

        part1 = MIMEText(html, 'html')
        msg.attach(part1)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
	
        print(i, dkp, date," price: ", next_price)

        if m > 0:
            cursor.execute("SELECT price FROM product WHERE id = '%s'" % m)
            recordss = cursor.fetchall()
            recc = str(recordss)
            price_aa = recc.replace("[", "").replace("(", "").replace(",", "").replace(")", "").replace("]", "")
            perv_price = int(price_aa)

            if next_price < perv_price:
                print("Discount!")
                discount_amount = next_price - perv_price
                print(discount_amount)
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "Digikala Price Tracker"
                msg['From'] = from_address
                msg['To'] = to_address

                html = """
                        <!DOCTYPE html>
                        <html>
                        <head></head>
                        <body>
                        <h1>Discount!</h1>
                        <p>{url}</p>
                        </body>
                        </html>
                       """.format(url=url)

                part1 = MIMEText(html, 'html')
                msg.attach(part1)
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(username,password)
                server.sendmail(from_address, to_address, msg.as_string())
                server.quit()
            
            if perv_price < next_price:
                print("Over Price")
                price_amount = perv_price - next_price
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "Digikala Price Tracker"
                msg['From'] = from_address
                msg['To'] = to_address

                html = """
                        <!DOCTYPE html>
                        <html>
                        <head></head>
                        <body>
                        <h1>Over Price</h1>
                        <p>{url}</p>
                        </body>
                        </html>
                       """.format(url=url)

                part1 = MIMEText(html, 'html')
                msg.attach(part1)
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(username,password)
                server.sendmail(from_address, to_address, msg.as_string())
                server.quit()
                     
    time.sleep(minutes)