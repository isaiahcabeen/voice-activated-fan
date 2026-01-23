🎤 Voice-Activated Fan

This project allows you to control a fan using voice commands.
By saying “fan on” or “fan off”, a Python program recognizes speech and sends commands to an Arduino, which controls a motor.

🧠 How It Works (Simple Explanation)

1. Python listens to your microphone (through the Mac microphone)

2. Vosk converts your voice into text

3. If the text matches a command, Python sends a signal to Arduino.

4. Arduino turns the motor on or off.


🔌 Wiring/Schematic Diagram:
<img width="1304" height="1160" alt="image" src="https://github.com/user-attachments/assets/453bc928-79bd-47f2-ade6-4e00c863b936" />
<img width="1418" height="428" alt="image" src="https://github.com/user-attachments/assets/535b453e-577a-4c79-8317-df5315d70816" />


⚙️ Hardware Required

Arduino UNO R4 Wifi

DC motor 

TA6586 - Motor Driver Chip

Jumper wires

Power Supply Module

USB-c cable


💻 Software Requirements (Mac)

Python libraries (in terminal): pip install pyserial sounddevice vosk

New-ish version of Python - https://www.python.org/ftp/python/3.14.2/python-3.14.2-macos11.pkg

Arduino IDE (use ai to figure out which download link you need)- https://www.arduino.cc/en/software/

Vosk speech model - https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
