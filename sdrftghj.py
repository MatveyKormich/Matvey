from bs4 import BeautifulSoup
import requests, lxml, json, sqlite3

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": "Skyrim",
    "hl": "en",  # language
    "gl": "us",  # country of the search, US -> USA
    "start": 0,  # number page by default up to 0
    # "filter": 0         # show all pages by default up to 10
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
soup = BeautifulSoup(html.text, 'lxml')

organic_results = []

for index, result in enumerate(soup.select(".tF2Cxc"), start=1):
    organic_results.append({
        'position': index,
        'title': result.select_one("h3").text,
        'link': result.select_one(".yuRUbf a").get('href'),
        'snippet': result.select_one(".VwiC3b").text if result.select_one(".VwiC3b") else None
    })

print(json.dumps(organic_results, indent=2, ensure_ascii=False))
