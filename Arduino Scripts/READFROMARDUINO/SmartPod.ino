#include "DHT.h"
#define DHTPIN 2     // DHT sensor connected to digital pin 2
#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);

const int humiditySensorPin= 0; //humidity sensor is connected to analog pin A0
void setup() {
Serial.begin(9600); //sets the baud rate for data transfer in bits/second
pinMode(humiditySensorPin, INPUT);
dht.begin();

}
void loop() {
delay(4000);

int liquid_level= analogRead(humiditySensorPin); //reads sensor value from analog humidity sensor
float h = dht.readHumidity(); // reads air humidity from the DHT sensor
float t = dht.readTemperature(); // reads temperature from the DHT sensor

Serial.print(liquid_level);
Serial.print(F(" "));
Serial.print(h);
Serial.print(F(" "));
Serial.println(t);
  
}
