#include <Wire.h>
#include <SPI.h>
#include <Adafruit_BMP280.h>

//all the pins can be chosen as wishes
#define BMP_SCK  (13) //SCK
#define BMP_MISO (10) //SDO
#define BMP_MOSI (12) //SDI
#define BMP_CS   (11) //CS

//Adafruit_BMP280 bmp(BMP_CS); //HARDWARE SPI
Adafruit_BMP280 bmp(BMP_CS, BMP_MOSI, BMP_MISO,  BMP_SCK);

void setup() {
  Serial.begin(9600);

  if (!bmp.begin()) {
    Serial.println(F("Could not find a valid BMP280 sensor, check wiring!"));
    while (1);
  }

  /* Default settings from datasheet. */
  bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,     /* Operating Mode. */
                  Adafruit_BMP280::SAMPLING_X2,     /* Temp. oversampling */
                  Adafruit_BMP280::SAMPLING_X16,    /* Pressure oversampling */
                  Adafruit_BMP280::FILTER_X16,      /* Filtering. */
                  Adafruit_BMP280::STANDBY_MS_500); /* Standby time. */
}

void loop() {
    Serial.print(String(bmp.readTemperature()) + "," + String(bmp.readPressure()) + "," + String(bmp.readAltitude(1023)) + "\n");
    delay(1000);
}
