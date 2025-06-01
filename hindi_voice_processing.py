import streamlit as st
from hindi_speech_to_text import recognize_hindi_speech, list_microphones
from nlp_processor import process_text  # This can be used for translation
from morse_code import text_to_morse
from morse_sound import play_morse, stop_morse
from transformers import MarianMTModel, MarianTokenizer
import torch



def translate_hi_en(text):
    model_name = "Helsinki-NLP/opus-mt-hi-en"
    if "marian_tokenizer" not in st.session_state:
        st.session_state["marian_tokenizer"] = MarianTokenizer.from_pretrained(model_name)
    if "marian_model" not in st.session_state:
        st.session_state["marian_model"] = MarianMTModel.from_pretrained(model_name)
    tokenizer = st.session_state["marian_tokenizer"]
    model = st.session_state["marian_model"]
    batch = tokenizer([text], return_tensors="pt", padding=True)
    with torch.no_grad():
        gen = model.generate(**batch)
    return tokenizer.decode(gen[0], skip_special_tokens=True)

def process_hindi_voice_tab():
    st.header("Voice to Morse Code")

    mic_names = list_microphones()
    mic_index = st.selectbox("Select Microphone", options=range(len(mic_names)), format_func=lambda i: mic_names[i], key="hindi_mic_select")

    # Initialize session state variables
    if "hindi_transcribed_text" not in st.session_state:
        st.session_state["hindi_transcribed_text"] = ""
    if "translated_text" not in st.session_state:
        st.session_state["translated_text"] = ""

    # When button clicked, get transcribed Hindi and translated English
    if st.button("Start Listening", key="hindi_voice_start"):
        hindi_text = recognize_hindi_speech(device_index=mic_index)
        translated_text = translate_hi_en(hindi_text)  # Use MarianMT for translation

        st.session_state["hindi_transcribed_text"] = hindi_text
        st.session_state["translated_text"] = translated_text

    # Editable Hindi transcription field
    st.text_area("Transcribed Hindi Text:", value=st.session_state.get("hindi_transcribed_text", ""), height=100, key="hindi_voice_text")

    # Editable Translated English field
    translated_text = st.text_area("Translated English Text:", value=st.session_state.get("translated_text", ""), height=100, key="english_translated_text")
    st.session_state["translated_text"] = translated_text  # update if edited

    # Generate Morse code from English text
    morse_code = text_to_morse(translated_text)
    st.text_area("Morse Code (From Translation):", value=morse_code, height=100, key="translated_morse_code")

    # Buttons to play/stop Morse
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Play Morse Sound", key="hindi_voice_play"):
            play_morse(translated_text)
    with col2:
        if st.button("Stop Sound", key="hindi_voice_stop_sound"):
            stop_morse()
