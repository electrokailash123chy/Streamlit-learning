import streamlit as st
import requests

st.title("🌐 ESP32 LED Control Dashboard")

# Input: ESP32 URL (local IP or Ngrok public URL)
esp32_url = st.text_input("Enter ESP32 URL:", "http://192.168.18.108")  # replace with your ESP32 IP if on LAN

col1, col2 = st.columns(2)

with col1:
    if st.button("Turn ON LED"):
        try:
            response = requests.get(f"{esp32_url}/led/on")
            st.success(response.text)
        except:
            st.error("Failed to connect. Check ESP32 URL or internet.")

with col2:
    if st.button("Turn OFF LED"):
        try:
            response = requests.get(f"{esp32_url}/led/off")
            st.success(response.text)
        except:
            st.error("Failed to connect. Check ESP32 URL or internet.")
