import streamlit as st
from morse_code import morse_to_text

def morse_verification_tab():
    st.header("Morse Code Verification")
    morse_input = st.text_area("Paste Morse Code Here:", height=100)
    if st.button("Decode to English"):
        decoded = morse_to_text(morse_input)
        st.success(f"Decoded English: {decoded}")