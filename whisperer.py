import os
from dotenv import load_dotenv
import whisper

# Load variables from .env file
load_dotenv()

model = whisper.load_model("base")
options = whisper.DecodingOptions(language="es")
result = model.transcribe("audio.mp3")
print(result["text"])
