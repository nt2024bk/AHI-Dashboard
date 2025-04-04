import streamlit as st
import pandas as pd
import os

st.title("🔗 Resources & Medical Support")

csv_path = "data/doctors.csv"

if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
    try:
        doctors = pd.read_csv(csv_path)
    except Exception as e:
        st.error(f"Error reading doctors.csv: {e}")
        doctors = pd.DataFrame()
else:
    # Fallback if CSV is missing or empty
    doctors = pd.DataFrame({
        'name': ['Dr. Jane Doe', 'Dr. Mark Silva'],
        'specialty': ['Neurology', 'Trauma & TBI'],
        'location': ['New York, USA', 'Toronto, Canada'],
        'contact': ['jane.doe@clinic.org', 'mark.silva@neuroclinic.ca'],
        'source': [
            'https://example.com/havana-doe',
            'https://example.com/havana-silva'
        ]
    })

if doctors.empty:
    st.warning("No doctor data available.")
else:
    st.subheader("🧑‍⚕️ Doctor Directory")
    st.dataframe(doctors)

    st.markdown("### 🔗 Mentioned In Articles")
    if "source" in doctors.columns:
        for index, row in doctors.iterrows():
            st.markdown(f"- [{row['name']}]({row['source']})")

st.markdown("### 🌐 Other Helpful Resources")
st.markdown("""
- [NIH on Neurological Syndromes](https://www.nih.gov/)
- [VA Havana Syndrome Support](https://www.va.gov/)
- [Directed Energy FAQ](https://example.com/directed-energy)
""")
