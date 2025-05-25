import streamlit as st
from speech_to_text import recognize_speech, list_microphones
from nlp_processor import process_text
from morse_code import text_to_morse
from morse_sound import play_morse, stop_morse

def process_voice_tab():
    st.header("Voice to Morse Code")

    mic_names = list_microphones()
    mic_index = st.selectbox("Select Microphone", options=range(len(mic_names)), format_func=lambda i: mic_names[i])

    if "voice_text" not in st.session_state:
        st.session_state["voice_text"] = ""
    if "processed_text" not in st.session_state:
        st.session_state["processed_text"] = ""

    # When button clicked, get new recognized text
    if st.button("Start Listening", key="voice_start"):
        recognized_text = recognize_speech(device_index=mic_index)
        st.session_state["voice_text"] = recognized_text
        st.session_state["processed_text"] = recognized_text

    # Editable text area for recognized text
    st.text_area("Recognized Text:", value=st.session_state["voice_text"], height=100, key="voice_text")

    # Update session state with user edits from text area
    # (Streamlit updates session_state automatically by key)

    # NLP processing button: updates processed_text
    if st.button("Process with NLP", key="voice_nlp_btn"):
        st.session_state["processed_text"] = process_text(st.session_state["voice_text"])

    # Show processed text info
    st.info(f"Processed Voice Text: {st.session_state.get('processed_text', '')}")

    # Convert to Morse and show
    morse_code = text_to_morse(st.session_state.get("processed_text", ""))
    st.text_area("Morse Code (Voice):", value=morse_code, height=100)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Play Morse Sound", key="voice_play"):
            play_morse(st.session_state.get("processed_text", ""))
    with col2:
        if st.button("Stop Sound", key="voice_stop_sound"):
            stop_morse()
