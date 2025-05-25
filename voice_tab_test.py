import streamlit as st
from speech_to_text import recognize_speech, list_microphones
from nlp_processor import process_text
from morse_code import text_to_morse
from morse_sound import play_morse, stop_morse

def process_voice_tab():
    st.header("Voice to Morse Code")

    mic_names = list_microphones()
    mic_index = st.selectbox("Select Microphone", options=range(len(mic_names)), format_func=lambda i: mic_names[i]["name"])

    if "voice_text" not in st.session_state:
        st.session_state.voice_text = ""
    if "processed_text" not in st.session_state:
        st.session_state.processed_text = ""

    # Start Listening button
    if st.button("Start Listening"):
        # Call your speech recognition
        recognized_text = recognize_speech(device_index=mic_index)
        st.session_state.voice_text = recognized_text
        st.session_state.processed_text = recognized_text

    st.text_area("Recognized Text:", value=st.session_state.voice_text, height=100)

    # NLP processing section
    if st.checkbox("Use NLP Processing (Voice)"):
        if st.button("Process Voice Text with NLP"):
            st.session_state.processed_text = process_text(st.session_state.voice_text)

    st.info(f"Processed Text: {st.session_state.processed_text}")

    # Morse code display
    morse_code = text_to_morse(st.session_state.processed_text)
    st.text_area("Morse Code (Voice):", value=morse_code, height=100)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Play Morse Sound (Voice)"):
            play_morse(st.session_state.processed_text)
    with col2:
        if st.button("Stop Sound (Voice)"):
            stop_morse()
