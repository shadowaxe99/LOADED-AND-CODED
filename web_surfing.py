import requests
from bs4 import BeautifulSoup

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # TODO: Extract useful information from the soup
        return soup.prettify()
    else:
        return None