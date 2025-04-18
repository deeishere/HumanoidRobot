#include <ESP32Servo.h>
Servo myservo;

int posVal;
int shoulderPin = 12;//brown
int FwdPin = 26,BwdPin=32;//right (Green-light blue)
int ActTime = 1000; 
int MaxSpd = 250; 
const int TrigPin = 13; // define TrigPin
const int EchoPin = 14; // define EchoPin.

void setup() {
  myservo.attach(12);
  pinMode(TrigPin , OUTPUT); // set trigPin to output mode
  pinMode(EchoPin , INPUT); // set echoPin to input mode
  Serial.begin(9600)
}

void loop() {

  digitalWrite(TrigPin , HIGH);
  delayMicroseconds(10);
  
  digitalWrite(TrigPin , LOW);
  
  duration = pulseIn(EchoPin , HIGH);
  
  distance = (duration/2) / 28.5 ;
  if (distance < 50){
  
      for (posVal = 120; posVal <= 180; posVal += 1) { 
        myservo.write(posVal); 
        delay(50);
      }
  
    analogWrite(FwdPin,MaxSpd); 
    delay(ActTime);
    analogWrite(FwdPin,0);
    analogWrite(BwdPin,MaxSpd); 
     delay(ActTime);
    analogWrite(BwdPin,0);
    
    for (posVal = 180; posVal >= 120; posVal -= 1) { 
      myservo.write(posVal); 
      delay(50); 
}


