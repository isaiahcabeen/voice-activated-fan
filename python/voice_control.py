// Pin definitions for motor driver
const int motorFI = 9;   // Forward input (PWM speed control)
const int motorBI = 10;  // Backward input (kept LOW since we only spin one direction)

void setup() {
  // Configure motor control pins as outputs
  pinMode(motorFI, OUTPUT);
  pinMode(motorBI, OUTPUT);

  // Ensure backward pin is always LOW (no reverse rotation)
  digitalWrite(motorBI, LOW);

  // Start serial communication with Python (baud rate: 9600)
  Serial.begin(9600);

  // Motor starts in OFF state
  analogWrite(motorFI, 0);
}

void loop() {
  // Check if data is available from Python
  if (Serial.available() > 0) {

    // Read command sent over serial until newline character
    String command = Serial.readStringUntil('\n');
    command.trim();  // Remove whitespace/newline characters

    // Turn fan ON at full speed
    if (command == "FAN_ON") {
      analogWrite(motorFI, 255);  // Max PWM value = full speed
      Serial.println("Motor ON");
    }

    // Turn fan OFF
    else if (command == "FAN_OFF") {
      analogWrite(motorFI, 0);    // PWM = 0 stops motor
      Serial.println("Motor OFF");
    }
  }
}

