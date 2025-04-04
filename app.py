from utils.scrape_news import search_google_news

keywords = [
    "Havana Syndrome",
    "Anomalous health incidents",
    "Directed energy attacks",
    "Embassy staff illnesses",
    "Unexplained neurological symptoms",
    "Diplomatic health incidents"
]

st.header("📰 Auto-Scraped Headlines (Extended Keywords)")
articles = search_google_news(keywords, max_results=20)

for article in articles:
    st.markdown(f"**[{article['headline']}]({article['url']})**")
    st.caption(article['snippet'])
