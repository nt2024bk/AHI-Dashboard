# 6_Resources.py
import streamlit as st
import pandas as pd
import os

st.title("🔗 Resources & Medical Support")

csv_path = "data/doctors.csv"

doctors = pd.DataFrame()
if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
    try:
        doctors = pd.read_csv(csv_path)
    except Exception as e:
        st.error(f"Error reading doctors.csv: {e}")

if doctors.empty:
    st.warning("No doctors mentioned in recent news articles.")
else:
    st.subheader("🧑‍⚕️ Doctor Directory")
    st.dataframe(doctors)

    if "source" in doctors.columns:
        st.markdown("### 🔗 Sources Mentioning Doctors")
        for index, row in doctors.iterrows():
            st.markdown(f"- [{row['name']}]({row['source']})")

st.markdown("### 🌐 Additional Resources")
st.markdown("""
- [NIH on Neurological Syndromes](https://www.nih.gov/)
- [VA Havana Syndrome Support](https://www.va.gov/)
- [Directed Energy FAQ](https://example.com/directed-energy)
- [National Academies: Health Effects of Directed Energy](https://www.nationalacademies.org/our-work/health-effects-of-directed-energy-exposures)
- [Microwave Auditory Effect Research (PubMed)](https://pubmed.ncbi.nlm.nih.gov/?term=microwave+auditory+effect)
- [Brain Injury Association of America](https://www.biausa.org/)
- [Medical Whistleblower Advocacy Network](http://medicalwhistleblower.org/)
- [Congressional Research Service: Havana Syndrome Reports](https://crsreports.congress.gov/)
""")
