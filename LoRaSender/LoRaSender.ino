#include <SPI.h>
#include <LoRa.h>

int counter = 0;
int sf = 12;
void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("LoRa Sender");
  
  

  if (!LoRa.begin(865E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
  LoRa.setTxPower(14);
}

void loop() {
  Serial.print("Sending packet: ");
  Serial.println(counter);
  
  
  if(counter % 110 == 0){
    sf = 12 - (counter / 110) % 6;
    LoRa.setSpreadingFactor(sf);

  }

  delay(500);

  // send packet
  LoRa.beginPacket();
  LoRa.println(counter);
  LoRa.print("spreading factor ");
  LoRa.println(sf);
  LoRa.endPacket();

  counter++;

  
}
