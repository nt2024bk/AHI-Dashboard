import streamlit as st
from utils.scrape_news import search_google_news

st.header("📰 Auto-Scraped Headlines (Havana Syndrome)")
articles = search_google_news()

for article in articles:
    st.markdown(f"**[{article['headline']}]({article['url']})**")
    st.caption(article['snippet'])
