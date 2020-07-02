import requests
from bs4 import BeautifulSoup

URL = 'https://suap.ifsp.edu.br/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())