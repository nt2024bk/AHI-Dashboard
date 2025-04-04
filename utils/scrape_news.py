import streamlit as st
from utils.scrape_news import search_google_news

st.title("📰 Auto-Scraped Headlines (Havana Syndrome & Related Terms)")

keywords = [
    "Havana Syndrome",
    "Anomalous health incidents",
    "Directed energy attacks",
    "Embassy staff illnesses",
    "Unexplained neurological symptoms",
    "Diplomatic health incidents"
]

try:
    articles = search_google_news(keywords, max_results=20)

    if articles:
        for article in articles:
            st.markdown(f"**[{article['headline']}]({article['url']})**")
            st.caption(article['snippet'])
    else:
        st.info("No articles found. Try expanding keywords or checking RSS sources.")

except Exception as e:
    st.error(f"News scraping failed: {e}")
