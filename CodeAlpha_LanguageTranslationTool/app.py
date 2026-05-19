import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

text = st.text_area("Enter Text")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "French": "fr",
    "Spanish": "es"
}

source = st.selectbox("Source Language", list(languages.keys()))
target = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter text")

    else:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translated Text:")
        st.write(translated)