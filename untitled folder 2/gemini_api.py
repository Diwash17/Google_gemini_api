import google.generativeai as genai
import os
from gtts import gTTS
from api_key_secret import *
# api_key="Your_api_Key"
genai.configure(api_key=API_KEY)

# Generate content using the model
prompt=input("Enter the prompt\n")


# Assuming there's a generate_text function directly available in the library
response = genai.generate_text(prompt=prompt)


generated_text = response.result 

tts = gTTS(text=generated_text, lang='en')

# Save the audio file
audio_file = "response.mp3"
tts.save(audio_file)

# Play the audio file
os.system(f"start {audio_file}")  

print("Response has been converted to speech and is being played.")
