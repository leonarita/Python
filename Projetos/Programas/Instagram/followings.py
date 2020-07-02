from bs4 import BeautifulSoup
import requests


def scrape_data(username):
    r = requests.get(URL.format(username))
    s = BeautifulSoup(r.text, "html.parser")
    meta = s.find("meta", property="og:description")
    print(s.prettify())


URL = "https://www.instagram.com/{}/following/"


if __name__ == "__main__":
    username = input("Informe o seu username: ")
    scrape_data(username)