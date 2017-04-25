#include <ArduinoJson.h>
#include <Servo.h>

Servo servoPitch;
Servo servoRoll;  
String json;

int currentPositionMotorRoll = 30;
int currentPositionMotorPitch = 30;

int correctPosition(int value){
  if(value > 90){
    value = 90;
  }
  else if (value < 0){
    value = 0; 
  }
  return value;
}

void setup() {
  Serial.begin(9600);

  servoPitch.attach(10); 
  //servoRoll.attach(10); 
  servoPitch.write(currentPositionMotorPitch);
  //servoRoll.write(currentPositionMotorRoll);
  
  while (!Serial) {
    // wait serial port initialization
  }

  Serial.println("Hello !!!!!");

  /*StaticJsonBuffer<200> jsonBuffer;
  char json[] =
      "{\"sensor\":\"gps\",\"time\":1351824120,\"data\":[48.756080,2.302038]}";
  JsonObject& root = jsonBuffer.parseObject(json);
  if (!root.success()) {
    Serial.println("parseObject() failed");
    return;
  }
  const char* sensor = root["sensor"];
  long time = root["time"];
  double latitude = root["data"][0];
  double longitude = root["data"][1];
  Serial.println(sensor);
  Serial.println(time);
  Serial.println(latitude, 6);
  Serial.println(longitude, 6);
  */
}

void loop() {
  // put your main code here, to run repeatedly:

  while (Serial.available() > 0) {
    json = Serial.readString();
    Serial.println(json);
    StaticJsonBuffer<200> jsonBuffer;
    JsonObject& root = jsonBuffer.parseObject(json);
    if (!root.success()) {
      Serial.println("parseObject() failed");
      return;
    }
    String action = root["action"];
    int degreesNumber = root["degrees"];
    Serial.println(action);
    Serial.println(degreesNumber);
    if(action.equals("moveHeadRight")){
      Serial.println("You write moveHeadRight");
      currentPositionMotorPitch = correctPosition(currentPositionMotorPitch + degreesNumber);
      Serial.println(currentPositionMotorPitch);
      servoPitch.write(currentPositionMotorPitch);
    }
    else if (action.equals("moveHeadLeft")){
      Serial.println("You write moveHeadLeft");
      currentPositionMotorPitch = correctPosition(currentPositionMotorPitch - degreesNumber);
      Serial.println(currentPositionMotorRoll);
      servoPitch.write(currentPositionMotorPitch);
    }
    else if (action.equals("moveHeadDown")){
      Serial.println("You write moveHeadDown");
      currentPositionMotorRoll = correctPosition(currentPositionMotorRoll + degreesNumber);
      Serial.println(currentPositionMotorRoll);
      servoRoll.write(currentPositionMotorRoll);
    }
    else if (action.equals("moveHeadUp")){
      Serial.println("You write moveHeadUp");
      currentPositionMotorRoll = correctPosition(currentPositionMotorRoll - degreesNumber);
      Serial.println(currentPositionMotorRoll);
      servoRoll.write(currentPositionMotorRoll);
    }
    else{
      Serial.println("NYI");
    }
  }
}
