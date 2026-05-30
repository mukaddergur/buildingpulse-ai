import streamlit as st
import websocket
import json
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")
st.title("BuildingPulse AI - Kontrol Paneli")

col_btn, col_alert = st.columns([1, 4])
with col_btn:
    if st.button("Akışı Başlat"): st.session_state.running = True
    if st.button("Akışı Durdur"): st.session_state.running = False

m1, m2, m3 = st.columns(3)
m_durum = m1.empty()
m_risk = m2.empty()
m_co2 = m3.empty()


g1, g2 = st.columns(2)
graph_temp_co2 = g1.empty()
graph_hum_light = g2.empty()
table_placeholder = st.empty()

if 'running' not in st.session_state: st.session_state.running = False

if st.session_state.running:
    ws = websocket.create_connection("ws://localhost:8000/ws/sensors")
    logs = []
    
    while st.session_state.running:
        data = json.loads(ws.recv())
        logs.append(data)
        if len(logs) > 10: logs.pop(0)
        df = pd.DataFrame(logs)
   
        m_durum.metric("Mevcut Durum", "Dolu" if data['predicted_occupancy'] == 1 else "Boş")
        m_risk.metric("Risk Skoru", data['risk_score'])
        m_co2.metric("CO2 Seviyesi", data['CO2'])
        fig1 = px.line(df, x='time', y=['Temperature', 'CO2'], title="Sıcaklık ve CO2")
        graph_temp_co2.plotly_chart(fig1, use_container_width=True)
        fig2 = px.line(df, x='time', y=['Humidity', 'Light'], title="Nem ve Işık")
        graph_hum_light.plotly_chart(fig2, use_container_width=True)
        table_placeholder.table(df.tail(5))