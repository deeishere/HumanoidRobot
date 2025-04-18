#include <Servo.h>  // Standard Servo library for Arduino Uno

Servo myservo;
int posVal=120;
int shoulderPin = 9;  // Use a PWM pin for the servo (9, 10, or 11 on Uno)
int FwdPin = 6, BwdPin = 5;  // Use PWM pins for the motor
int ActTime = 1000;
int MaxSpd = 255;  // 0-255 for PWM control

void setup() {
  myservo.attach(shoulderPin);  // Attach servo to pin 9
  pinMode(FwdPin, OUTPUT);  // Set motor control pins as output
  pinMode(BwdPin, OUTPUT);
  Serial.begin(9600);  // Start serial communication for debugging
}

void loop() {


  // Move servo from 120° to 180°
  for (posVal = 120; posVal <= 180; posVal++) {
    myservo.write(posVal);  // Move servo to position
    delay(100);  // Longer delay to ensure smooth movement and allow servo time to adjust
    Serial.print("Moving to: ");
    Serial.println(posVal);  // Debugging: Track servo position
  }

 


  // Move servo from 180° back to 120°
  for (posVal = 180; posVal >= 120; posVal--) {
    myservo.write(posVal);  // Move servo to position
    delay(100);  // Longer delay to ensure smooth movement
    Serial.print("Moving back to: ");
    Serial.println(posVal);  // Debugging: Track servo position
  }

  // Optional: Add a delay to avoid continuously looping
  delay(2000);  // Add a small delay before repeating the loop
}
