#include <IRremote.h>
int RECV_PIN = 2;

int STBY = 10; 

int PWMA = 3; //Speed control 
int AIN1 = 9; //Direction
int AIN2 = 8; //Direction

int PWMB = 5; 
int BIN1 = 11; 
int BIN2 = 12;

IRrecv irrecv(RECV_PIN);

decode_results results;

void setup(){
  pinMode(STBY, OUTPUT);

  pinMode(PWMA, OUTPUT);
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);

  pinMode(PWMB, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  Serial.begin(9600);
  irrecv.enableIRIn();  
}

void loop(){
  if (irrecv.decode(&results)) {
    Serial.println(results.value);
    if (results.value == 16609423)
    {
      move(1, 255, 1);
      move(2, 255, 1);
      delay(1000);
      stop();
    }
    if (results.value == 16625743){
      move(1, 255, 0);
      move(2, 255, 0);
      delay(1000);
      stop();
    }
    if (results.value == 16601263){
      move(1, 255, 0);
      move(2, 255, 1);
      delay(1000);
      stop();
    }
    if (results.value == 16617583){
      move(1, 255, 1);
      move(2, 255, 0);
      delay(1000);
      stop();
    }    
    irrecv.resume();  
  }  

}

void move(int motor, int speed, int direction){

  digitalWrite(STBY, HIGH);

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
  }
  else{
    digitalWrite(BIN1, inPin1);
    digitalWrite(BIN2, inPin2);
    analogWrite(PWMB, speed);
  }
}

void stop(){  
  digitalWrite(STBY, LOW);
}

