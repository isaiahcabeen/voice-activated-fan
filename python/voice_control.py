import serial
import time
import sounddevice as sd
import vosk
import queue
import json

arduino = serial.Serial('/dev/cu.usbmodemF0F5BD56516C2', 9600)
time.sleep(2)

model = vosk.Model("model")
samplerate = 16000
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, dtype='int16',
                       channels=1, callback=callback):
    rec = vosk.KaldiRecognizer(model, samplerate)
    print("Say 'Fan On' or 'Fan Off'...")

    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "")
            print("You said:", text)

            if "fan on" in text:
                arduino.write(b"FAN_ON\n")
                print("Motor ON command sent")
            elif "fan off" in text:
                arduino.write(b"FAN_OFF\n")
                print("Motor OFF command sent")

