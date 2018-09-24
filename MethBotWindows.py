import requests
import re
import webbrowser
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\SeleniumDrivers\chromedriver.exe')



#this will be an input
#keyword = 't-shirts'
def testparameters():
    global category
    global colour
    global keyword
    global checkoutdelay
    global autofilldelay
    category = 'jackets'
    colour = ('black').title()
    keyword = ('Bone Varsity Jacket')
    checkoutdelay = float(4.5)
    autofilldelay = float(5)
testparameters()

def realtest():
    global category
    global colour
    global keyword
    global checkoutdelay
    global autofilldelay
    category = input('category: \n ')
    colour = input('colour: \n ')
    keyword = input('keyword: \n')
    checkoutdelay = float(input('checkout delay: \n'))
    autofilldelay = int(input('autofill delay: \n'))

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
driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()

time.sleep(0.1)
driver.find_element_by_link_text('checkout now').click()
time.sleep(0.1)
#now in checkout


(driver.find_element_by_id("order_billing_name")).send_keys("Testing Name")
time.sleep(autofilldelay/14)
(driver.find_element_by_id("order_email")).send_keys("testing@gmail.com")
time.sleep(autofilldelay/14)
(driver.find_element_by_id("order_tel")).send_keys("01234 567890")
time.sleep(autofilldelay/14)
(driver.find_element_by_id("bo")).send_keys("123 Test Street")
time.sleep(autofilldelay/14)
(driver.find_element_by_id("oba3")).send_keys("Testing")
time.sleep(autofilldelay/14)
(driver.find_element_by_id("order_billing_address_3")).send_keys("More test")
time.sleep(autofilldelay/14)
(driver.find_element_by_id("order_billing_city")).send_keys("London")
time.sleep(autofilldelay/14)
(driver.find_element_by_id("order_billing_zip")).send_keys("TE1 1ST")
time.sleep(autofilldelay/14)
(driver.find_element_by_id("cnb")).send_keys("1234 1234 1234 1234")
time.sleep(autofilldelay/14)
(driver.find_element_by_id("vval")).send_keys("123")
time.sleep(autofilldelay/14)
(driver.find_element_by_id("credit_card_type")).send_keys("Visa")
time.sleep(autofilldelay/14)
(driver.find_element_by_id("credit_card_month")).send_keys("01")
time.sleep(autofilldelay/14)
(driver.find_element_by_id("credit_card_year")).send_keys("2020")
time.sleep(autofilldelay/14)





#finds the number of articles, then goes through that number looking for the 'keyword' data. Then it traces back to the url and takes that. 

#data = ((((str(response.json())).split("[{'definition':"))[1]).split("'"))[1]

