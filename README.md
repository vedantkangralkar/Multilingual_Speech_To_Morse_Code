# 🚀 Multilingual Speech to Morse Code

This project builds a multilingual speech-to-Morse code converter leveraging OpenAI’s Whisper model fine-tuned on Hindi speech, combined with NLP techniques and translation models. It converts speech and text inputs—especially Hindi audio—into Morse code with options for preprocessing and verification.

---

## 🧠 Model Training and Fine-Tuning

We fine-tuned **OpenAI’s Whisper Small** model on the Hindi subset of the **Mozilla Common Voice 11.0** dataset, containing crowd-sourced spoken audio clips with transcripts, ideal for Automatic Speech Recognition (ASR).

**Training Setup:**

- Base Model: Whisper Small (transformer-based ASR)
- Framework: Hugging Face Transformers with `Seq2SeqTrainer`
- Batch Size: 16
- Learning Rate: 1e-5
- Training Steps: 4000 (~9–10 epochs)
- Mixed precision (fp16) and gradient checkpointing enabled
- Total training time: ~7.3 hours on GPU
- Final training loss: ~0.079

**Deployment:**

- Model saved locally: `./whisper-small-vedant-nlp`
- Hosted on Hugging Face Model Hub:  
  [vedant-2012/whisper-small-vedant-nlp](https://huggingface.co/vedant-2012/whisper-small-vedant-nlp)

---

## 🧩 Application Modules

The project features four main interactive modules (tabs):

### 🟦 Tab 1: Text to Morse

- Input: Plain text
- Output: Morse code translation using standard key mappings
- Optionally applies NLP preprocessing such as stop word removal with NLTK

### 🟧 Tab 2: Voice to Morse Code (English)

- Input: English audio recording + user confirmation
- Uses pretrained Whisper Base for speech-to-text transcription
- Optional NLP preprocessing (stop word removal)
- Converts processed text into Morse code

### 🟨 Tab 3: Hindi Voice to Morse Code

- Input: Hindi speech audio
- Transcription by fine-tuned Whisper Small model
- Translates Hindi text to English using MarianMT (Helsinki-NLP)
- Converts English translation to Morse code

### 🟩 Tab 4: Verification

- Converts Morse code back to text using reverse mappings
- Verifies accuracy of Morse code translations

---

## 🎯 Use Cases

- Educational tools to learn Morse code and speech processing
- Accessibility aids for speech-to-text-to-Morse communication
- Emergency or military communication systems
- Cross-lingual speech recognition and translation applications

---

## 📦 Installation and Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/multilingual-speech-to-morse.git
   cd multilingual-speech-to-morse
