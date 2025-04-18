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

   // Forward motor movement
  analogWrite(FwdPin, MaxSpd);  // Set motor speed to max (255)
  delay(ActTime);  // Run motor for ActTime (1000 ms)
  analogWrite(FwdPin, 0);  // Stop motor

 

  // Reverse motor movement
  analogWrite(BwdPin, MaxSpd);  // Set motor speed to max (255)
  delay(ActTime);  // Run motor for ActTime (1000 ms)
  analogWrite(BwdPin, 0);  // Stop motor


  

  // Optional: Add a delay to avoid continuously looping
  delay(2000);  // Add a small delay before repeating the loop
}
