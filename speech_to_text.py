import vosk
import sys
import sounddevice as sd
import queue
import json
import time
from main import respond
model = vosk.Model("model_small")
samplerate = 16000
device = 1

q = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def listen(response_function):
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
                           channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                voice = rec.Result()

                voice = voice[14:-3]
                response_function(str(voice))



