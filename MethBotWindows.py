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