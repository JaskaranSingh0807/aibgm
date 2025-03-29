import streamlit as st
import requests
import io
import soundfile as sf


API_URL = "https://router.huggingface.co/hf-inference/models/facebook/musicgen-small"
HEADERS = {"Authorization": "Bearer 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"}  

def generate_music(prompt):

    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    if response.status_code == 200:
        return response.content  
    else:
        st.error("Error: Could not generate music. Try again later.")
        return None


st.title("🎶 AI Music Generator")
st.write("Generate AI-based music by entering a description!")

prompt = st.text_input("Enter a music description")

if st.button("Generate Music"):
    if prompt:
        audio_bytes = generate_music(prompt)
        if audio_bytes:
            st.audio(io.BytesIO(audio_bytes), format='audio/wav')
    else:
        st.warning("Please enter a description before generating music.")
