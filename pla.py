from unidecode import unidecode
import multiprocessing
from datetime import datetime
from playwright.sync_api import sync_playwright
import argparse
import os
import warnings
import sqlite3
import time
import threading

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description= 'Digikala Discount Warning', prog= 'ddw.py')
parser.add_argument('--dkp', type=str, help= 'Set Digikala Product ID', metavar= 'dkp-14563541', required=True)
parser.add_argument('--delay', type=str, help='Set Delay(in minutes)', metavar= '5', required=True)
parser.add_argument('--count', type=int, help='Set Counter(how many time to scrape)', metavar= '10', required=True)
args = parser.parse_args()

dkp = args.dkp
delay = args.delay
count = args.count


minutes = int(delay) * 60


url = "https://www.digikala.com/product/" + dkp

for i in range(0, count):
    i += 1
    m = i - 1
    dir = os.getcwd()
    dirr = dir +"\\"+ "database\\" + dkp
    dirrr = dirr + "\\" + dkp + ".png"
    dirrrr = dirr + "\\" + dkp + ".db"
    
    if not os.path.exists(dirr):
       os.makedirs(dirr)
    
    if not os.path.exists(dirrrr):
       with open(dirrrr, 'w') as fp:
            pass
        
    connection = sqlite3.connect(dirrrr)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS product (id INTEGER, name TEXT,dkp TEXT,date  TEXT, price INTEGER)")
    
       
    with sync_playwright() as p:
        browser = p.chromium.launch()
        now = datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")        
        page = browser.new_page()
        page.goto(url)
        
        try:
            price_a = page.locator('xpath=//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[2]/div[2]/div[2]/span')
            price_b = unidecode(price_a.text_content())
            price_c = price_b.replace(",", "")
            price_one = int(price_c)
        except:
            price_one = 9999999999
                    
        try:    
            price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div/div[4]/div/div/div/div[1]/div/div[2]/span')
            price_b = unidecode(price_a.text_content())
            price_c = price_b.replace(",", "")
            price_two = int(price_c)
        except:
            price_two = 9999999999
                    
        try:
            price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div/div[4]/div/div/div/div[1]/div[2]/div[1]/span')
            price_b = unidecode(price_a.text_content())
            price_c = price_b.replace(",", "")
            price_three = int(price_c)
        except:
            price_three = 9999999999
                    
        try:
            price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[1]/div[2]/div[1]/span')
            price_b = unidecode(price_a.text_content())
            price_c = price_b.replace(",", "")
            price_four = int(price_c)
        except:
            price_four = 9999999999
                    
        try:
            price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[2]/div[2]/div[1]/span')
            price_b = unidecode(price_a.text_content())
            price_c = price_b.replace(",", "")
            price_five = int(price_c)
        except:
            price_five = 9999999999
                    
        try:
            price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div/div[4]/div/div/div/div[1]/div[2]/div[2]/span')
            price_b = unidecode(price_a.text_content())
            price_c = price_b.replace(",", "")
            price_six = int(price_c)
        except:
            price_six = 9999999999
                
        try:
            price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[2]/div/div[2]/span')
            price_b = unidecode(price_a.text_content())
            price_c = price_b.replace(",", "")
            price_seven = int(price_c)
        except:
            price_seven = 9999999999
            
        try:
            price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[1]/div/div[2]/span')
            price_b = unidecode(price_a.text_content())
            price_c = price_b.replace(",", "")
            price_eight = int(price_c)
        except:
            price_eight = 9999999999
            
        try:
            price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[1]/div[2]/div[2]/span')
            price_b = unidecode(price_a.text_content())
            price_c = price_b.replace(",", "")
            price_nine = int(price_c)
        except:
            price_nine = 9999999999
        
        try: 
            price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[3]/div[5]/div/div[4]/div/div/div/div[1]/div/div[1]/span')
            price_b = unidecode(price_a.text_content())
            price_c = price_b.replace(",", "")
            price_ten = int(price_c) 
        except:
            price_ten = 9999999999
            
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
                
        price_list = [price_one, price_two, price_three, price_four, price_five, price_six, price_seven, price_eight, price_nine, price_ten]
        price_main = min(price_list)
        
        insert_query = """INSERT INTO product(id, name, dkp, date, price) VALUES (?, ?, ?, ?, ?);"""
        data_query = (i, product_name, dkp, date, price_main)
        cursor.execute(insert_query, data_query)
        connection.commit()
        
        cursor.execute("SELECT price FROM product WHERE id = '%s'" % i)
        records = cursor.fetchall()
        rec = str(records)
        price_a = rec.replace("[", "").replace("(", "").replace(",", "").replace(")", "").replace("]", "")
        next_price = int(price_a)
        print(i, dkp, date," price: ", next_price)
    
        if m > 0:
            cursor.execute("SELECT price FROM product WHERE id = '%s'" % m)
            recordss = cursor.fetchall()
            recc = str(recordss)
            price_aa = recc.replace("[", "").replace("(", "").replace(",", "").replace(")", "").replace("]", "")
            perv_price = int(price_aa)
        
            if next_price < perv_price:
                print("Discount!")
    
    time.sleep(minutes)
    
"""
xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div/div[4]/div/div/div/div[1]/div/div[1]/span

PS C:\Users\11\Desktop\monitor> py .\pla.py --dkp dkp-12924184 --count 50 --delay 30
1 dkp-12924184 2024-09-28 23:39:31  price:  9999999999

"""