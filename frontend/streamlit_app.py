import streamlit as st
import requests

st.title("GenAI Live Call Insights")

uploaded_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

if uploaded_file:
    st.audio(uploaded_file)
    with st.spinner("Analisando áudio..."):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/analyze-audio/", files=files)
        if response.ok:
            data = response.json()
            st.subheader("Transcrição:")
            st.write(data["transcript"])
            st.subheader("Sugestões:")
            st.write(data["insights"])
