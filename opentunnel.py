import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

runcode = True

while (runcode):
    html = urlopen('file:///Users/fin/Desktop/Scraper/htmlsandbox.html')
    page = BeautifulSoup(html.read(), 'html.parser')
    string = str(page)
    result = string[string.find("<!--")+len("<!--"):string.rfind("-->")]
    exec(result)
    print("running...")

print("\n  Code ran succesfully. \n")