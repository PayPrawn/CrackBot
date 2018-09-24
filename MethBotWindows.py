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
    category = 'jackets'
    colour = ('black').title()
    keyword = ('Bone Varsity Jacket')
testparameters()

def realtest():
    global category
    global colour
    global keyword
    category = input('category:\n ')
    colour = input('colour: \n ')
    keyword = input('keyword: \n')

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
driver.find_element_by_id("order_billing_name")
name.send_keys("Testing Name")
name = driver.find_element_by_id("order_email")
name.send_keys("testing@gmail.com")
name = driver.find_element_by_id("order_tel")
name.send_keys("01234 567890")
name = driver.find_element_by_id("bo")
name.send_keys("123 Test Street")
name = driver.find_element_by_id("oba3")
name.send_keys("Testing")
name = driver.find_element_by_id("order_billing_address_3")
name.send_keys("More test")
name = driver.find_element_by_id("order_billing_city")
name.send_keys("London")
name = driver.find_element_by_id("order_billing_zip")
name.send_keys("TE1 1ST")
name = driver.find_element_by_id("cnb")
name.send_keys("1234 1234 1234 1234")
name = driver.find_element_by_id("vval")
name.send_keys("123")
name = driver.find_element_by_id("credit_card_type")
name.send_keys("Visa")
name = driver.find_element_by_id("credit_card_month")
name.send_keys("01")
name = driver.find_element_by_id("credit_card_year")
name.send_keys("2020")






#finds the number of articles, then goes through that number looking for the 'keyword' data. Then it traces back to the url and takes that. 

#data = ((((str(response.json())).split("[{'definition':"))[1]).split("'"))[1]

