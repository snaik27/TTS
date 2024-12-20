import torch
import re
from TTS.api import TTS

# Check if CUDA is installed
if torch.cuda.is_available():
    print("CUDA installed successfully\n") 
else:
    print("CUDA not properly installed. Stopping process...")
    quit()

# Print available TTS models
view_models = input("View models? [y/n]\n")
if view_models == "y":
    tts_manager = TTS().list_models()
    all_models = tts_manager.list_models()
    print("TTS models:\n", all_models, "\n", sep = "")

# Prompt model selection
model = input("Enter model:\n")
# for example, tts_models/multilingual/multi-dataset/xtts_v2

# Example voice cloning with selected model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tts = TTS((model), progress_bar=True).to(device)
textFile = "C:\\Github\\TTS\\screenplay.txt"
counter = 0
try:
    with open(textFile, 'r') as file:
        while True:
            lines = [file.readline().strip() for _ in range(10)]
            if not any(lines):
                break

            line = "".join(lines)
            #cleanedline = re.sub(r'[^a-zA-Z0-9.!\s]', '', line)
            tts.tts_to_file(line, speaker_wav= "C:\\Github\\TTS\\tests\\data\\ljspeech\\wavs\\LJ001-0001.mp3",
                    language="en", file_path=f"output{counter}.wav")
            counter = counter + 1
except FileNotFoundError:
    print(f"File {textFile} doesn't exist")
