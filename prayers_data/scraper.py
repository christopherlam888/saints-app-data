from .prayer import Prayer

import requests
from bs4 import BeautifulSoup
from cleantext import clean

base_url = "https://www.catholic.org/prayers/prayer.php?p="

headers = {"Accept-Language": "en-US, en;q=0.5"}

def scrape_page(p):
    name = ""
    content = ""
    results = requests.get(base_url + p, headers=headers, timeout=5)
    soup = BeautifulSoup(results.text, "html.parser")
    name = soup.find("h1", class_="page-title").text
    content = soup.find("div", class_="col-sm-12").text
    content = clean(content, lower=False, no_line_breaks=False)
    content = content[content.find("Printable PDF")+14:]
    content = content.replace("\n", "\n\n")
    return Prayer(name, content)
