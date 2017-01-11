int LED_PIN = 13;
String value;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0) {
    value = Serial.readString();
    Serial.println(value);
    if(value == "a"){
      Serial.println("You write a");
      digitalWrite(LED_PIN, HIGH);
    }
    else if (value == "z"){
      Serial.println("You write z");
      digitalWrite(LED_PIN, LOW);
    }
  }

}
