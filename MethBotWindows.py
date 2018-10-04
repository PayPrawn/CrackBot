import requests
import re
import webbrowser
import time
import os
from selenium import webdriver
import threading
from threading import Thread

driver = webdriver.Chrome(executable_path='C:\SeleniumDrivers\chromedriver.exe')
starttime = time.time()
runcode = True
realtime = ''

#this will be an input
#keyword = 't-shirts'
def testparameters():
    global category
    global colour
    global keyword
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
    global googleusername
    global googlepassword
    global refreshdelay
    category = 'sweatshirts'
    refreshdelay = 10 #milliseconds
    colour = ('Black').title()
    keyword = ('Jewels Hooded Sweatshirt')
    name = 'Finlay Scott'
    email = 'finlay.scott@rocketmail.com'
    phone = '07568566185'
    address1 = '24 Prestonville Road'
    address2 = ''
    address3 = ''
    city = 'Brighton'
    zipcode = 'BN13TL'
    ccnumber = '1234 1234 1234 134'
    cvv = '123'
    cardtype = 'Visa'
    cardmonth = '01'
    cardyear = '2021'
    googleusername = 'finlay.scott123@gmail.com'
    googlepassword = 'Stanley2002'
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

def currenttime():
    global displaytime
    global realtime
    currenttime = time.localtime()
    string = str(currenttime)
    hour = string.split("tm_hour=")[1].split(',')[0]
    minute = string.split('tm_min=')[1].split(',')[0]
    sec = string.split('tm_sec=')[1].split(',')[0]
    realtime = hour + ':' + minute + ':' + sec
    if int(minute) < 10:
        displayminute = '0' + minute
    else:
        displayminute = minute
    if int(hour) < 10: 
        displayhour = '0' + hour
    else:
        displayhour = hour
    if int(sec) < 10:
        displaysecond = '0' + sec
    else:
        displaysecond = sec
    displaytime = '[' + displayhour + ':' + displayminute + ':' + displaysecond + ']'

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
    #driver.find_element_by_xpath('//*[@id="pay"]/input')).click()

def geturl():
    global new_url
    correcturl = 'repeat'
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

#time

currenttime()
print(displaytime + ' logging into google...')
driver.get('https://accounts.google.com/ServiceLogin/identifier?hl=en-gb&flowName=GlifWebSignIn&flowEntry=AddSession')

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(googleusername)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(googlepassword)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
currenttime()
print(displaytime + ' dodging captcha...')
time.sleep(1)
driver.get('https://www.youtube.com/watch?v=u9PNq6Gd8Mg')
time.sleep(1)
#supreme
bing = "bing"
while realtime != '10:43:45' and bing != "bing":
    time.sleep(1)
    currenttime()
    print(displaytime + ' waiting for drop... ')
currenttime()
print(displaytime + ' starting autofill...')
while True:
    try:
        get_url()
        print(new_url)
        total = new_url + " "
        break
    except NameError:
        time.sleep(1)
        print('waiting for website')
driver.find_element_by_xpath('//*[@id="size"]').send_keys('Large')
driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
time.sleep(0.1)
driver.find_element_by_link_text('checkout now').click()
autofill()
#if __name__=='__main__':
   #  p1 = Process(target = fillname())
   #  p1.start()
    # p2 = Process(target = fillemail())
     #p2.start()
     #p3 = Process(target = fillphone())
     #p3.start()
#now in checkout
currenttime()
print(displaytime + ' complete.')
runtime = time.time() - starttime
print(runtime)






#finds the number of articles, then goes through that number looking for the 'keyword' data. Then it traces back to the url and takes that. 

#data = ((((str(response.json())).split("[{'definition':"))[1]).split("'"))[1]

#now in checkout