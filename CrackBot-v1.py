import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.supremenewyork.com/shop/all')
page = BeautifulSoup(html.read(), 'html.parser')
string = str(page)
print(string)
