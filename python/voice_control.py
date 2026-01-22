"""
Voice-controlled fan using Python, Vosk speech recognition, and Arduino.
Listens for voice commands ("fan on", "fan off") and sends serial commands to Arduino.
"""

import serial        # Serial communication with Arduino
import time          # Used for delay to allow Arduino to initialize
import sounddevice as sd  # Microphone audio input
import vosk          # Offline speech recognition engine
import queue         # Thread-safe queue for audio data
import json          # Parsing Vosk recognition results

# ---------- Arduino Serial Connection ----------
# NOTE: Change this port to match your Arduino device
arduino = serial.Serial('/dev/cu.usbmodemF0F5BD56516C2', 9600)
time.sleep(2)  # Wait for Arduino to reset and be ready

# ---------- Speech Recognition Setup ----------
model = vosk.Model("model")  # Load offline speech recognition model
samplerate = 16000           # Sample rate required by Vosk
q = queue.Queue()            # Queue to store incoming audio data

def callback(indata, frames, time, status):
    """
    This function is called automatically by sounddevice
    whenever new audio data is captured from the microphone.
    """
    if status:
        print(status)  # Print any audio stream errors or warnings
    
    # Convert audio data to bytes and store it in the queue
    q.put(bytes(indata))

# ---------- Microphone Audio Stream ----------
with sd.RawInputStream(
    samplerate=samplerate,
    blocksize=8000,
    dtype='int16',
    channels=1,
    callback=callback
):
    # Initialize the speech recognizer
    rec = vosk.KaldiRecognizer(model, samplerate)
    print("Say 'Fan On' or 'Fan Off'...")

    # Main loop: continuously process audio and detect commands
    while True:
        data = q.get()  # Get audio data from the queue

        # Check if a complete phrase has been recognized
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())  # Convert recognition result to JSON
            text = result.get("text", "")      # Extract recognized text
            print("You said:", text)

            # ---------- Voice Command Handling ----------
            if "fan on" in text:
                arduino.write(b"FAN_ON\n")  # Send command to Arduino
                print("Motor ON command sent")

            elif "fan off" in text:
                arduino.write(b"FAN_OFF\n")  # Send command to Arduino
                print("Motor OFF command sent")

