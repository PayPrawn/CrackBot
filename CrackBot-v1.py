from bs4 import BeautifulSoup
import urllib
url = 'https://www.supremenewyork.com/shop/all'
page = urllib.urlopen(url) 
soup = BeautifulSoup(page, 'html.parser')
string = str(soup)
print(string)