import requests
import re
import webbrowser
import time
from selenium import webdriver
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
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
time.sleep(10)
elem = driver.find_elements_by_xpath('//*[@id="add-remove-buttons"]/input')
elem.click()
driver.close()





#finds the number of articles, then goes through that number looking for the 'keyword' data. Then it traces back to the url and takes that. 

#data = ((((str(response.json())).split("[{'definition':"))[1]).split("'"))[1]
#https://www.supremenewyork.com/shop/all/(category)