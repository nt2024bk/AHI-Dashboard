
import streamlit as st
import pandas as pd

st.title("📜 Government Responses & Policy Actions")

data = pd.read_csv("data/gov_updates.csv") if "data/gov_updates.csv" else pd.DataFrame({
    'date': ['2024-11-20', '2025-01-12'],
    'country': ['USA', 'UK'],
    'action': ['Legislation introduced for victim support', 'Parliamentary inquiry initiated']
})

st.dataframe(data)
