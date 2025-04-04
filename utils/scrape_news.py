import feedparser
import spacy
from datetime import datetime
import re

# Load spaCy NLP model (install with: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# Expanded search term list
keywords = [
    "Havana Syndrome",
    "Anomalous health incidents",
    "Directed energy attacks",
    "Microwave weapon injuries",
    "Neurological attack embassy",
    "Unexplained neurological symptoms",
    "Embassy staff illness unexplained",
    "Cognitive damage in diplomats",
    "Brain injury foreign service",
    "Psychotronic weapons",
    "Microwave auditory effect",
    "Symptoms from sonic weapons",
    "Non-lethal weapons health effect",
    "Foreign service trauma symptoms",
    "Energy weapon directed at personnel",
    "US diplomats mysterious illness",
    "Cognitive impairment unexplained",
    "White matter brain anomalies",
    "Bizarre illness foreign officials"
]

def search_google_news(queries=keywords, max_results=20):
    """
    Searches Google News RSS for multiple keyword queries and returns article metadata.
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
                "date": entry.get("published", datetime.now().isoformat()),
                "query": query
            })

    return articles


def extract_doctors_from_articles(articles):
    """
    Extracts names of doctors from article text using spaCy NLP (PERSON entities prefixed with Dr./Doctor).
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
