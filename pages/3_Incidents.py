import streamlit as st
import pandas as pd
import os

st.title("📋 Havana Syndrome Incident Reports")

csv_path = "data/incidents.csv"

if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
    data = pd.read_csv(csv_path)
else:
    data = pd.DataFrame({
        'date': ['2025-01-10', '2025-02-05'],
        'location': ['Berlin', 'Madrid'],
        'symptoms': ['Dizziness, ringing ears', 'Fatigue, pressure'],
        'details': [
            'Diplomatic staff affected near consulate.',
            'Unusual sound heard before neurological symptoms.'
        ]
    })

st.dataframe(data)
