#include <Wire.h>
#include "paj7620.h"

#define I2C_ADDR 0x27 //I2C adress, you should use the code to scan the adress first (0x27) here
#define BACKLIGHT_PIN 3 // Declaring LCD Pins
#define En_pin 2
#define Rw_pin 1
#define Rs_pin 0
#define D4_pin 4
#define D5_pin 5
#define D6_pin 6
#define D7_pin 7

#define GES_REACTION_TIME    500
#define GES_ENTRY_TIME      800
#define GES_QUIT_TIME     1000



void setup() {
  paj7620Init();
  Serial.begin(9600);

}


void loop() {


  uint8_t data = 0, data1 = 0, error;

  error = paj7620ReadReg(0x43, 1, &data);       // Read Bank_0_Reg_0x43/0x44 for gesture result.
  if (!error)
  {

    switch (data)                   // When different gestures be detected, the variable 'data' will be set to different values by paj7620ReadReg(0x43, 1, &data).
    {
      case GES_RIGHT_FLAG:
        delay(GES_ENTRY_TIME);
        paj7620ReadReg(0x43, 1, &data);
        if (data == GES_FORWARD_FLAG)
        {

          Serial.print("Forward");
          delay(GES_QUIT_TIME);
        }
        else if (data == GES_BACKWARD_FLAG)
        {
            
          Serial.print("Backward");
          delay(GES_QUIT_TIME);
        }
        else
        {
          
          Serial.print("Right");
        }
        break;
      case GES_LEFT_FLAG:
        delay(GES_ENTRY_TIME);
        paj7620ReadReg(0x43, 1, &data);
        if (data == GES_FORWARD_FLAG)
        {
          
          Serial.print("Forward");
          delay(GES_QUIT_TIME);
        }
        else if (data == GES_BACKWARD_FLAG)
        {
          
          Serial.print("Backward");
          delay(GES_QUIT_TIME);
        }
        else
        {
          
          Serial.print("Left");
        }
        break;
      case GES_UP_FLAG:
        delay(GES_ENTRY_TIME);
        paj7620ReadReg(0x43, 1, &data);
        if (data == GES_FORWARD_FLAG)
        {
            
            Serial.print("Forward");
          delay(GES_QUIT_TIME);
        }
        else if (data == GES_BACKWARD_FLAG)
        {
            
            Serial.print("Backward");
          delay(GES_QUIT_TIME);
        }
        else
        {
            
            Serial.print("Up");
        }
        break;
      case GES_DOWN_FLAG:
        delay(GES_ENTRY_TIME);
        paj7620ReadReg(0x43, 1, &data);
        if (data == GES_FORWARD_FLAG)
        {
            
            Serial.print("Forward");
          delay(GES_QUIT_TIME);
        }
        else if (data == GES_BACKWARD_FLAG)
        {
            
            Serial.print("Backward");
          delay(GES_QUIT_TIME);
        }
        else
        {
            
            Serial.print("Down");
        }
        break;
      case GES_FORWARD_FLAG:
          
          Serial.print("Forward");
        delay(GES_QUIT_TIME);
        break;
      case GES_BACKWARD_FLAG:
          
          Serial.print("Backward");
        delay(GES_QUIT_TIME);
        break;
      case GES_CLOCKWISE_FLAG:
          
          Serial.print("Clockwise");
        break;
      case GES_COUNT_CLOCKWISE_FLAG:
          
          Serial.print("anti-clockwise");
        break;
      default:
        paj7620ReadReg(0x44, 1, &data1);
        if (data1 == GES_WAVE_FLAG)
        {
            
            Serial.print("wave");
        }
        break;
    }
  }

  delay(100);

}
