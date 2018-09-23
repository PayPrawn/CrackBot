import requests
category = 't-shirts'
#this will be an input
#keyword = 't-shirts'
response = (requests.get('https://www.supremenewyork.com/shop/all/t-shirts')).text
x = response.split('<a class="name-link"')
x = x[1]
x = x.split('</a>')
x = x[0]
x = x.split('">')
x = x[1]
print(x)


#data = ((((str(response.json())).split("[{'definition':"))[1]).split("'"))[1]
#https://www.supremenewyork.com/shop/all/(category)