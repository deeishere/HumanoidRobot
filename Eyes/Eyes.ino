#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>

// TFT screen pins

 //right eye
#define TFT_CS   27   
#define TFT_RST  12   
#define TFT_DC   25   
#define TFT_SCLK 14   
#define TFT_MOSI 13  // sda in the screen

// left eye
#define TFT_CS1   5 
#define TFT_RST1  4
#define TFT_DC1   2
#define TFT_SCLK1 18   
#define TFT_MOSI1 23 

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_MOSI, TFT_SCLK, TFT_RST); // right eye
Adafruit_ST7735 tft1 = Adafruit_ST7735(TFT_CS1, TFT_DC1, TFT_MOSI1, TFT_SCLK1, TFT_RST1); // left eye
// Define colors
#define BLACK      ST77XX_BLACK
#define WHITE      ST77XX_WHITE
#define RED        ST77XX_RED
#define BABY_BLUE  0x4C9A  // Slightly darker baby blue
int eyeColor = WHITE;
int pupilColor = BLACK;
void setup() {
  Serial.begin(9600);
  tft.initR(INITR_BLACKTAB);
  tft.fillScreen(BLACK);
  tft1.initR(INITR_BLACKTAB);
  tft1.fillScreen(BLACK);
  
   tft.fillRoundRect(0, 0, 128, 160, 30, eyeColor);
   tft1.fillRoundRect(0, 0, 128, 160, 30, eyeColor);
}

void drawSadEye() {
// Left Eye (Slanted)
  //tft1.fillTriangle(20, 0, 20, 160, 120, 160, eyeColor);  // Slanted rectangle effect
  tft1.fillRoundRect(0, 0, 128, 160, 30, eyeColor);
 tft1.fillCircle(28, 0, 100, pupilColor);
  //tft.fillCircle(55, 65, 6, pupilColor);  // Pupil

  // Right Eye (Slanted)
 // tft.fillTriangle(120, 160, 20, 160, 120, 0, eyeColor);
 tft.fillRoundRect(0, 0, 128, 160, 30, eyeColor);
 tft.fillCircle(100, 0, 100, pupilColor);
  // Angry Eyebrows (Red & Slanted)
  //tft.drawLine(30, 50, 70, 40, RED);  // Left eyebrow
  //tft.drawLine(90, 40, 130, 50, RED);  // Right eyebrow
}
void drawHappyEye(){
  //left
   tft1.fillRoundRect(0, 0, 128, 160, 30, eyeColor);
  tft1.fillCircle(64, 160, 90, pupilColor);

  //right
  tft.fillRoundRect(0, 0, 128, 160, 30, eyeColor);
  tft.fillCircle(64, 160, 90, pupilColor);
}

void noramlEyes(){
  tft1.fillRoundRect(0, 0, 128, 160, 30, eyeColor);
  tft.fillRoundRect(0, 0, 128, 160, 30, eyeColor);
}

void drawExitedEye(){
  tft1.fillRoundRect(0, 0, 128, 160, 30, eyeColor);
  tft1.fillCircle(64, 160, 110, pupilColor);

  //right
  tft.fillRoundRect(0, 0, 128, 160, 30, eyeColor);
  tft.fillCircle(64, 160, 110, pupilColor);
}
void Angry(){
  tft1.fillRoundRect(0, 0, 128, 160, 30, eyeColor);
  tft1.fillCircle(100, 0, 100, pupilColor);

  tft.fillRoundRect(0, 0, 128, 160, 30, eyeColor);
  tft.fillCircle(28, 0, 100, pupilColor);
}


void loop(){
 //drawSadEye();

  drawHappyEye(); 
  delay(5000);
  //noramlEyes();
  //delay(1000);
  drawSadEye();
  delay(5000);
  drawExitedEye();
  delay(5000);
  Angry();
  delay(5000);
}


 
