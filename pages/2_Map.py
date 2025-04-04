
import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("📍 Global Havana Syndrome Heatmap")

data = pd.DataFrame({
    'lat': [38.8951, 51.5074, -33.8688],
    'lon': [-77.0364, -0.1278, 151.2093],
    'location': ['Washington DC', 'London', 'Sydney'],
    'date': ['2024-12-01', '2025-01-15', '2025-02-20'],
    'description': [
        'Reported case near embassy.',
        'Symptoms experienced by diplomat.',
        'Unusual auditory phenomena recorded.'
    ]
})

st.subheader("🗺️ Map of Reported Cases")
st.map(data[['lat', 'lon']])

st.subheader("🔥 Global Heatmap")
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=20,
        longitude=0,
        zoom=1,
        pitch=30,
    ),
    layers=[
        pdk.Layer(
            'HeatmapLayer',
            data=data,
            get_position='[lon, lat]',
            get_weight=1,
            radiusPixels=60,
        )
    ]
))
