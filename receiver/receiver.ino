#include <SPI.h>
#include <LoRa.h> 

int LED = 3;
String inString = "";    // string to hold input
 int sf = 0;
void setup() {
  Serial.begin(9600);
  pinMode(LED,OUTPUT);
  

  while (!Serial);
  Serial.println("LoRa Receiver");
  if (!LoRa.begin(865E6)) { // or 915E6
    Serial.println("Starting LoRa failed!");
    while (1);
  }

  LoRa.setSpreadingFactor(12);
  }
 int counter = 0;
void loop() {
  
  // try to parse packet
  int packetSize = LoRa.parsePacket();
  if (packetSize) { 
    // read packet    
    while (LoRa.available())
    { 
      inString = LoRa.readString();    
    }
       
    Serial.print("rssi ");
    Serial.print(LoRa.packetRssi()); 
    Serial.print(" ");
    Serial.print(LoRa.packetSnr());
    Serial.print(" ");
    String s = "";
    Serial.print(inString); 
    // int f = 0;

    if((counter + 1) % 80 == 0) {sf += 1;
    sf %= 6;
    LoRa.setSpreadingFactor(11- sf);}
    inString = "";  
    counter++; 
  }
  analogWrite(LED, 1);
}