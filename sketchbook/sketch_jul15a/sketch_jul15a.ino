#include <Wire.h>
int dypOutputPin = 2; // TRIG
int dypInputPin = 3;  // ECHO
long distance;
long cm;
int STBY = 10; 
int PWMA = 5; 
int AIN1 = 9;
int AIN2 = 8;
int PWMB = 6;
int BIN1 = 11;
int BIN2 = 12;
void setup(){
  pinMode(dypOutputPin, OUTPUT);
  pinMode(dypInputPin,INPUT);
  pinMode(STBY, OUTPUT);
  pinMode(PWMA, OUTPUT);
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(PWMB, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);  
}

void loop()
{
  digitalWrite(dypOutputPin, LOW);
  delayMicroseconds(2);
  digitalWrite(dypOutputPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(dypOutputPin, LOW);   
  distance = pulseIn(dypInputPin, HIGH);
  cm= distance/58;                        

  if(cm<30){
    stop();
    move(1, 255, 1);
    move(2, 255, 0);  
    stop();    
  }else{
    move(1, 255, 1);
    move(2, 255, 1);
    stop();
    move(1, 128, 1);
    move(2, 128, 1);
    stop();    
  }
}
void move(int motor, int speed, int direction){

  digitalWrite(STBY, HIGH); //disable standby

  boolean inPin1 = LOW;
  boolean inPin2 = HIGH;

  if(direction == 1){
    inPin1 = HIGH;
    inPin2 = LOW;
  }

  if(motor == 1){
    digitalWrite(AIN1, inPin1);
    digitalWrite(AIN2, inPin2);
    analogWrite(PWMA, speed);
  }else{
    digitalWrite(BIN1, inPin1);
    digitalWrite(BIN2, inPin2);
    analogWrite(PWMB, speed);
  }
}

void stop(){
  digitalWrite(STBY, LOW);
}
