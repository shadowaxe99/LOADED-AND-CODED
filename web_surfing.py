import requests

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None