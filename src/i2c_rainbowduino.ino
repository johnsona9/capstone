#include <Rainbowduino.h>
#include <Wire.h>
#include "Rainbowduino.h"

uint32_t colors[64] = {0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000};
byte val1 = 0x00;
byte val2 = 0x00;
int oneReceived = 0;
int twoReceived = 0;
int suggested1 = -1;
int suggested2 = -1;
int counter = 0;

void setup()
{
  Rb.init();
  Wire.begin(4);                // join i2c bus with address #4
  Wire.onReceive(receiveEvent); // register event
  Serial.begin(115200);         // start serial for output
  Serial.println("hello!");
  Rb.setPixelXY(7, 7, 0xff00ff);
}



void loop()
{
  if (suggested1 != -1 && suggested2 != -1) {
    if (millis() % 3000 == 0) {
      Rb.setPixelXY(suggested1 % 8, suggested1 / 8, 0xffffff);
      Rb.setPixelXY(suggested2 % 8, suggested2 / 8, 0xffffff);
    }
    else if (millis() % 1500 == 0) {
      Rb.setPixelXY(suggested1 % 8, suggested1 / 8, colors[suggested1]);
      Rb.setPixelXY(suggested2 % 8, suggested2 / 8, colors[suggested2]);
    }
  }
}

void receiveEvent(int howMany) {
  byte val = 0x00;
  int pos = 0;
  counter ++;
  while (Wire.available() > 0)
  {
    val = Wire.read();
  }
  if (oneReceived == 0 && twoReceived == 0) {
    val1 = val;
    oneReceived = 1;
  } else if (oneReceived == 1 && twoReceived == 0) {
    val2 = val;
    twoReceived = 1;
  }

  if (oneReceived == 1 && twoReceived == 1) {
    oneReceived = 0;
    twoReceived = 0;
    if (val1 == 0) {
      uint32_t LEDcolor = 0x000000;
      if (val2 < 64) {
        pos = val2;
      } else if (val2 < 128) {
        LEDcolor = 0xff0000;
        pos = val2 - 64;
      } else if (val2 < 192) {
        LEDcolor = 0x00ff00;
        pos = val2 - 128;
      } else {
        LEDcolor = 0x0000ff;
        pos = val2 - 192;
      }

      int row = pos / 8;
      int column = pos % 8;
      colors[pos] = LEDcolor;
      Rb.setPixelXY(column, row, LEDcolor);
    }
    else if (val1 == 1) {
      suggested1 = val2;
    } else if (val1 == 2) {
      suggested2 = val2;
    } else if (val1 == 3) {
      suggested1 = -1;
      suggested2 = -1;
    }
  }

  if (counter == 134) {
    for (int x = 0; x < 64; x ++) {
      Rb.setPixelXY(x % 8, x / 8, colors[x]);
    }
    counter = 0;
  }

}
