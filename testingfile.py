import requests
response = requests.get('https://www.supremenewyork.com/shop/all/jackets')
text = response.text
print(text)

