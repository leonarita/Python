import requests
from bs4 import BeautifulSoup
import json

headers = {'Mentioned In Next Slide'}
url = 'Amazon Product Page URL'

content = requests.get(url, headers=headers)
soup = BeautifulSoup(content.text, 'html.parser')

title = soup.select("#productTitle")[0].get_text().strip()
price = soup.select("#priceblock_ourprice")[0].get_text()

print(title, " ", price)