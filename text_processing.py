import streamlit as st
from nlp_processor import process_text
from morse_code import text_to_morse

def process_text_tab():
    st.header("Text to Morse Code")
    text_input = st.text_area("Enter text to convert to Morse code:", key="text_input")
    use_nlp = st.checkbox("Use NLP Processing", key="text_nlp")
    if "processed_text" not in st.session_state:
        st.session_state["processed_text"] = ""

    if use_nlp and text_input:
        if st.button("Process with NLP", key="text_nlp_btn"):
            st.session_state["processed_text"] = process_text(text_input)
        else:
            st.session_state["processed_text"] = text_input
        st.info(f"Processed Text: {st.session_state['processed_text']}")
    else:
        st.session_state["processed_text"] = text_input

    morse_code = text_to_morse(st.session_state["processed_text"])
    st.text_area("Morse Code:", value=morse_code, height=100)

    col1, col2 = st.columns(2)
    from morse_sound import play_morse, stop_morse
    with col1:
        if st.button("Play Morse Sound", key="text_play"):
            play_morse(st.session_state["processed_text"])
    with col2:
        if st.button("Stop Sound", key="text_stop"):
            stop_morse()