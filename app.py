import streamlit as st
from text_processing import process_text_tab
from voice_processing import process_voice_tab
from morse_verification import morse_verification_tab

st.set_page_config(page_title="Speech-to-Morse Code Converter", layout="centered")
st.title("🔊 Speech-to-Morse Code Converter")

tab1, tab2, tab3 = st.tabs(["Text", "Voice", "Verify Morse"])

with tab1:
    process_text_tab()
with tab2:
    process_voice_tab()
with tab3:
    morse_verification_tab()