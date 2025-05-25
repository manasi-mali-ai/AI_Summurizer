import requests
from bs4 import BeautifulSoup

def scrape_website_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    return " ".join(p.get_text() for p in paragraphs)
