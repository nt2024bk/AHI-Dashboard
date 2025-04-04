
import streamlit as st
import pandas as pd

st.title("🔗 Resources & Medical Support")

st.markdown("### 🧑‍⚕️ Doctors and Clinics")
doctors = pd.read_csv("data/doctors.csv") if "data/doctors.csv" else pd.DataFrame({
    'name': ['Dr. Jane Doe', 'Dr. Mark Silva'],
    'specialty': ['Neurology', 'Trauma & TBI'],
    'location': ['New York, USA', 'Toronto, Canada'],
    'contact': ['jane.doe@clinic.org', 'mark.silva@neuroclinic.ca']
})
st.dataframe(doctors)

st.markdown("### 🌐 Recommended Links")
st.markdown("""
- [NIH on Neurological Syndromes](https://www.nih.gov/)
- [VA Havana Syndrome Support Page](https://www.va.gov/)
- [Directed Energy FAQ](https://example.com/directed-energy)
""")
