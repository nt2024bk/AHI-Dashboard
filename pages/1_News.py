
import streamlit as st
import pandas as pd

st.title("📰 Havana Syndrome News Headlines")

# Placeholder for scraped headlines
news = [
    {"date": "2025-04-01", "headline": "New symptoms linked to directed energy incidents", "source": "Global News"},
    {"date": "2025-03-28", "headline": "Government briefings hint at foreign involvement", "source": "The Herald"},
]

st.write("### Latest Headlines")
for item in news:
    st.markdown(f"**{item['date']}** - [{item['headline']}]({item['source']})")
