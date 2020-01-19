import requests
from bs4 import BeautifulSoup

URL = "https://www.instagram.com/{}/"


def scrape(username):
    full_url = URL.format(username)  # make full URL
    r = requests.get(full_url)  # send GET requests
    s = BeautifulSoup(r.text, "lxml")  # make soup object

    tag = s.find("meta", attrs={"name": "description"})
    text = tag.attrs['content']  # grab the content text
    main_text = text.split("-")[0]  # required text

    return main_text


USERNAME = "3richkey"
data = scrape(USERNAME)
print(data)
