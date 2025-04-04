
import streamlit as st
import pandas as pd

st.title("📋 Havana Syndrome Incident Reports")

data = pd.read_csv("data/incidents.csv") if "data/incidents.csv" else pd.DataFrame({
    'date': ['2025-01-10', '2025-02-05'],
    'location': ['Berlin', 'Madrid'],
    'symptoms': ['Dizziness, ringing ears', 'Fatigue, pressure'],
    'details': [
        'Diplomatic staff affected near consulate.',
        'Unusual sound heard before neurological symptoms.'
    ]
})

st.dataframe(data)
