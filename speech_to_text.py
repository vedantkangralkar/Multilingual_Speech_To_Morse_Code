import sounddevice as sd
import soundfile as sf
from transformers import pipeline
import numpy as np

# Initialize the ASR pipeline (choose one model)
asr = pipeline("automatic-speech-recognition", model="openai/whisper-base")  # or "facebook/wav2vec2-base-960h"

def list_microphones():
    return sd.query_devices()

def recognize_speech(device_index=None, duration=5, samplerate=16000, filename="temp_audio.wav"):
    try:
        print("Recording...")
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16', device=device_index)
        sd.wait()
        sf.write(filename, audio, samplerate)
        print("Recording finished.")
        result = asr(filename)
        print(f"ASR result: {result}")
        print(result)
        return result["text"] if "text" in result else "[No text recognized]"
    except Exception as e:
        print(f"Error in recognize_speech: {e}")
        return f"[Error: {e}]"