import torch
import sounddevice as sd
import time

import config

LANGUAGE = 'en'
MODEL_ID = 'lj_16khz'
DEVICE = torch.device('cpu') # cpu or gpu
turn_on_text = f'Hello master. {config.ROBOTIK_NAME} just woke up from sleep, how can I help you?'

model, SYMBOLS, SAMPLE_RATE, _, apply_tts = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                           model='silero_tts',
                                                           language=LANGUAGE,
                                                           speaker=MODEL_ID)
model = model.to(DEVICE)

# Example
# audio = apply_tts(texts=[turn_on_text], sample_rate =SAMPLE_RATE, model=model, symbols=SYMBOLS, device=DEVICE)
# sd.play(audio[0], SAMPLE_RATE)
# time.sleep(len(audio[0]) / SAMPLE_RATE)
# sd.stop()

def robotik_speak(s: str):
    print("Robotik: " + s)
    audio = apply_tts(texts=[s], sample_rate=SAMPLE_RATE, model=model, symbols=SYMBOLS, device=DEVICE)
    sd.play(audio[0], SAMPLE_RATE)
    time.sleep(len(audio[0]) / SAMPLE_RATE)
    time.sleep(1)
    sd.stop()

