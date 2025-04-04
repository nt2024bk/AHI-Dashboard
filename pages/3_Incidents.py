# 3_Incidents.py
import streamlit as st
import pandas as pd
import os

st.title("📋 Havana Syndrome Incident Reports")

csv_path = "data/incidents.csv"

if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
    try:
        data = pd.read_csv(csv_path)
    except Exception as e:
        st.error(f"Error reading CSV: {e}")
        data = pd.DataFrame()
else:
    data = pd.DataFrame({
        'date': ['2025-01-10', '2025-02-05'],
        'location': ['Berlin', 'Madrid'],
        'symptoms': ['Dizziness, ringing ears', 'Fatigue, pressure'],
        'details': [
            'Diplomatic staff affected near consulate.',
            'Unusual sound heard before neurological symptoms.'
        ],
        'source_url': [
            'https://example.com/incident-berlin',
            'https://example.com/incident-madrid'
        ]
    })

if data.empty:
    st.warning("No incident data available.")
else:
    st.dataframe(data)
    st.markdown("### 🔗 Incident Sources")
    for url in data['source_url']:
        st.markdown(f"- [View Source]({url})")
