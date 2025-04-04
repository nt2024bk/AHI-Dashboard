import requests
from bs4 import BeautifulSoup

def search_google_news(query="havana syndrome", max_results=10):
    headers = {'User-Agent': 'Mozilla/5.0'}
    search_url = f"https://news.google.com/search?q={query.replace(' ', '%20')}"
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for item in soup.find_all('a', href=True):
        text = item.get_text().strip()
        if text and "articles" in item["href"]:
            link = "https://news.google.com" + item["href"][1:]
            articles.append({
                "headline": text,
                "url": link,
                "snippet": "Preview from Google News"
            })
            if len(articles) >= max_results:
                break
    return articles
