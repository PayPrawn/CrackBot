import requests
import re
import webbrowser
import time
import os
from selenium import webdriver
import threading
from threading import Thread
<<<<<<< HEAD
=======
import sys
>>>>>>> e680d647048b1d4538a9a087adb7777e398e5b10

driver = webdriver.Chrome(executable_path='C:\SeleniumDrivers\chromedriver.exe')
starttime = time.time()


#this will be an input
#keyword = 't-shirts'
def testparameters():
    global category
    global colour
    global keyword
    global checkoutdelay
    global autofilldelay
    global name
    global email
    global phone
    global address1
    global address2
    global address3S
    global city
    global zipcode
    global ccnumber
    global cvv
    global cardtype
    global cardmonth
    global cardyear
    category = 'jackets'
    colour = ('black').title()
    keyword = ('Bone Varsity Jacket')
    checkoutdelay = float(4.5)
    autofilldelay = float(5)
    name = 'Test Ing'
    email = 'test@gmail.com'
    phone = '01234 567890'
    address1 = 'test street'
    address2 = ''
    address3 = ''
    city = 'London'
    zipcode = 'TE1 1ST'
    ccnumber = '1234 1234 1234 1234'
    cvv = '123'
    cardtype = 'Visa'
    cardmonth = '01'
    cardyear = '2020'
testparameters()

def realtest():
    global category
    global colour
    global keyword
    global checkoutdelay
    global autofilldelay
    global name
    global email
    global phone
    global address1
    global address2
    global address3
    global city
    global zipcode
    global ccnumber
    global cvv
    global cardtype
    global cardmonth
    global cardyear
    category = input('category: \n ')
    colour = input('colour: \n ')
    keyword = input('keyword: \n')
    checkoutdelay = float(input('checkout delay: \n'))
    autofilldelay = int(input('autofill delay: \n'))
    name = input('name: \n')
    email = input('email: \n')
    phone = input('phone number: \n')
    address1 = input('address 1: \n')
    address2 = input('address 2: \n')
    address3 = input('address 3: \n')
    city = input('city: \n')
    zipcode = input('zip: \n')
    cardtype = input('card type: \n')
    ccnumber = input('card number: \n')
    cvv = input('cvv: \n')
    cardmonth = input('expiry month: \n')
    cardyear = input('expiry year: \n')

def fillname():
    (driver.find_element_by_xpath('//*[@id="order_billing_name"]')).send_keys(name)

def fillemail():
    (driver.find_element_by_xpath('//*[@id="order_email"]')).send_keys(email) 

def fillphone():
    (driver.find_element_by_xpath('//*[@id="order_tel"]')).send_keys(phone)

def autofill():
    (driver.find_element_by_xpath('//*[@id="order_billing_name"]')).send_keys(name)
    (driver.find_element_by_xpath('//*[@id="order_email"]')).send_keys(email)      

    (driver.find_element_by_xpath('//*[@id="order_tel"]')).send_keys(phone)
    (driver.find_element_by_xpath('//*[@id="bo"]')).send_keys(address1)
    if address1 != '':
        (driver.find_element_by_xpath('//*[@id="oba3"]')).send_keys(address2)
    if address2 != '':
        (driver.find_element_by_xpath('//*[@id="order_billing_address_3"]')).send_keys(address3)
    (driver.find_element_by_xpath('//*[@id="order_billing_city"]')).send_keys(city)
    (driver.find_element_by_xpath('//*[@id="order_billing_zip"]')).send_keys(zipcode)
    (driver.find_element_by_xpath('//*[@id="cnb"]')).send_keys(ccnumber)
    (driver.find_element_by_xpath('//*[@id="vval"]')).send_keys(cvv)
    (driver.find_element_by_xpath('//*[@id="credit_card_type"]')).send_keys(cardtype)
    (driver.find_element_by_xpath('//*[@id="credit_card_month"]')).send_keys(cardmonth)
    (driver.find_element_by_xpath('//*[@id="credit_card_year"]')).send_keys(cardyear)
    (driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins')).click()

url = 'https://www.supremenewyork.com/shop/all/' + category
r = requests.get(url)
response = r.text
keyword_split = response.split('<h1><a class="name-link"')
colour_split = response.split('<p><a class="name-link"')
number_of_articles = len(keyword_split)
for i in range(number_of_articles):
    if i != 0:    
        searched_k = (((keyword_split[i].split('">'))[1]).split('</a>'))[0]
        searched_c = (((colour_split[i].split('">'))[1]).split('</a>'))[0]
        if (searched_k == keyword) and (searched_c == colour):
            new_url = 'https://www.supremenewyork.com' +  (((keyword_split[i].split('href="'))[1]).split('">'))[0]

driver.get(new_url)
driver.find_element_by_xpath('//*[@id="size"]').send_keys('Large')
driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
time.sleep(0.1)
driver.find_element_by_link_text('checkout now').click()
py (Autofill.JS)
#autofill()
#if __name__=='__main__':
   #  p1 = Process(target = fillname())
   #  p1.start()
    # p2 = Process(target = fillemail())
     #p2.start()
     #p3 = Process(target = fillphone())
     #p3.start()
#now in checkout
runtime = time.time() - starttime
print(runtime)






#finds the number of articles, then goes through that number looking for the 'keyword' data. Then it traces back to the url and takes that. 

#data = ((((str(response.json())).split("[{'definition':"))[1]).split("'"))[1]

#now in checkout