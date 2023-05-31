from .saint import Saint

import requests
from bs4 import BeautifulSoup
import re
from cleantext import clean

base_url = "https://www.catholic.org"

headers = {"Accept-Language": "en-US, en;q=0.5"}

def add_spaces(text):
    return re.sub(r'(?<=[^\s\.\?!])([\.\?!])(?=[^\s])', r'\1 ', text)

def get_pages(page):
    pages = []
    results = requests.get(page, headers=headers, timeout=5)
    soup = BeautifulSoup(results.text, "html.parser")
    list_items_div = soup.find("div", id="saintPopular")
    list_items = list_items_div.find_all("li")
    for item in list_items:
        a = item.find("a")
        pages.append(base_url + a['href'])
    return pages

def scrape_page(page):
    name = ""
    feastday = ""
    content = ""
    failed = 0
    while True:
        results = requests.get(page, headers=headers, timeout=5)
        soup = BeautifulSoup(results.text, "html.parser")
        feastday = soup.find("div", class_="panel-body").text
        if "Feastday" in feastday or failed == 10:
            if failed == 10:
                feastday = "None"
            else:
                feastday = " ".join(feastday[11:].replace('\n', ' ').split((" "), 2)[:-1])
            name = soup.find("h1", class_="page-title").text
            content_parts = (soup.find("div", id="saintContent")).find_all("p")
            content = ""
            for part in content_parts:
                content += part.text
            content = add_spaces(content)
            content = clean(content, lower=False, no_line_breaks=True, no_urls=True)
            break
        else:
            failed += 1
    return Saint(name, feastday, content)
