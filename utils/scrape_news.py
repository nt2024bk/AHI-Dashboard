import feedparser
import spacy
from datetime import datetime
import re

# Load spaCy NLP model (make sure to install it: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

def search_google_news(queries, max_results=20):
    """
    Search Google News RSS for a list of keywords and return basic article info.
    """
    base_url = "https://news.google.com/rss/search?q="
    articles = []

    for query in queries:
        url = f"{base_url}{query.replace(' ', '+')}"
        feed = feedparser.parse(url)

        for entry in feed.entries[:max_results]:
            articles.append({
                "headline": entry.title,
                "url": entry.link,
                "snippet": entry.get("summary", "No snippet available"),
                "date": entry.get("published", datetime.now().isoformat())
            })

    return articles

def extract_doctors_from_articles(articles):
    """
    Run spaCy NLP on each article's title + snippet to extract names like 'Dr. John Smith'.
    """
    doctors = []

    for article in articles:
        text = article['headline'] + " " + article.get('snippet', '')
        doc = nlp(text)

        for ent in doc.ents:
            if ent.label_ == "PERSON":
                name = ent.text.strip()
                if re.match(r"^(Dr\\.|Doctor)\\s", name, re.IGNORECASE):
                    doctors.append({
                        "name": name,
                        "specialty": "Unknown",
                        "location": "Unknown",
                        "contact": "N/A",
                        "source": article['url']
                    })

    return doctors
