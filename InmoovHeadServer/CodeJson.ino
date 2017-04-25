
#include <aJSON.h>
char jsonString[] = "{\"data\":\"moveForward\",\"speedvalue\":36}";
String value;

void setup() {
Serial.begin(9600);
}

char* getValueForKey(char *jsonString, char *key) 
{
    char* value;

    aJsonObject* root = aJson.parse(jsonString);

    if (root != NULL) {
        //Serial.println("Parsed successfully 1 " );
        aJsonObject* data = aJson.getObjectItem(root, key); 

        if (data != NULL) {
            value = data->valuestring;
            Serial.println(value);
        }
    }

    if (value) {
        return value;
    } else {
        return NULL;
    }
}

void loop() {

  while (Serial.available() > 0) {
    //value = Serial.readString();
    char key[] = "data";
    value = getValueForKey(jsonString, key);
    Serial.println(value);
    if(value == "moveForward"){
      Serial.println("You write moveForward");
    }
    else if (value == "moveBackward"){
      Serial.println("You write moveBackward");
    }
  }
}
