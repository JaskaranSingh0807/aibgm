import streamlit as st
import io
import numpy as np
import soundfile as sf
from scipy.signal import sawtooth, square
import random

st.title("BGM Generator")

def generate_high_quality_music(duration=10, sample_rate=44100, genre="Ambient"):
    
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note_freqs = [220, 262, 294, 330, 349, 392, 440]  
    
    if genre == "Jazz":
        music_wave = sum(np.sin(2 * np.pi * (random.choice(note_freqs) + 5) * t) for _ in range(3))
        music_wave += sawtooth(2 * np.pi * 70 * t) * 0.4  
    elif genre == "Rock":
        music_wave = sum(square(2 * np.pi * random.choice(note_freqs) * t) for _ in range(3))
        music_wave += sawtooth(2 * np.pi * 90 * t) * 0.3  
    else:  
        music_wave = sum(np.sin(2 * np.pi * random.choice(note_freqs) * t) for _ in range(3))
        music_wave += np.sin(2 * np.pi * 40 * t) * 0.2 
    
    music_wave = (music_wave / np.max(np.abs(music_wave))) * 0.5 
    return music_wave, sample_rate

option = st.radio("Choose input type:", ("Upload Singing", "Enter Text", "Hum a Melody"))
genre = st.selectbox("Choose BGM Genre:", ["Jazz", "Rock", "Ambient"])

if option == "Upload Singing":
    uploaded_file = st.file_uploader("Upload your singing (WAV/MP3)", type=["wav", "mp3"])
    if uploaded_file and st.button("Generate AI Music"):
        music_wave, sr = generate_high_quality_music(genre=genre)
        output_buffer = io.BytesIO()
        sf.write(output_buffer, music_wave, sr, format='wav')
        output_buffer.seek(0)
        
        st.success("AI-generated background music is ready!")
        st.download_button("Download AI BGM (WAV)", data=output_buffer, file_name="ai_bgm.wav", mime="audio/wav")

elif option == "Enter Text":
    user_text = st.text_input("Enter lyrics or description:")
    if user_text and st.button("Generate AI Music"):
        music_wave, sr = generate_high_quality_music(genre=genre)
        output_buffer = io.BytesIO()
        sf.write(output_buffer, music_wave, sr, format='wav')
        output_buffer.seek(0)
        
        st.success("AI-generated background music is ready!")
        st.download_button("Download AI BGM (WAV)", data=output_buffer, file_name="ai_bgm.wav", mime="audio/wav")

elif option == "Hum a Melody":
    st.write("Feature coming soon: Hum a melody and generate AI music!")