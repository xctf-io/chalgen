//update from SAnwandter

#define ROW_1 2
#define ROW_2 3
#define ROW_3 4
#define ROW_4 5
#define ROW_5 6
#define ROW_6 7
#define ROW_7 8
#define ROW_8 9

#define COL_1 10
#define COL_2 11
#define COL_3 12
#define COL_4 13
#define COL_5 A0
#define COL_6 A1
#define COL_7 A2
#define COL_8 A3

const byte rows[] = {
    ROW_1, ROW_2, ROW_3, ROW_4, ROW_5, ROW_6, ROW_7, ROW_8
};
const byte col[] = {
  COL_1,COL_2, COL_3, COL_4, COL_5, COL_6, COL_7, COL_8
};

// The display buffer
// It's prefilled with a smiling face (1 = ON, 0 = OFF)
byte letters[][8] = {{B11111111,B11111111,B11111111,B11111111,B11111111,B11111111,B11111111,B11111111},  //All on
{B00000000,B00010000,B00010000,B00010000,B00010000,B00000000,B00010000,B00000000},  //All Off
{B00000000,B00111100,B01100110,B01100110,B01111110,B01100110,B01100110,B01100110}, //A
{B01111000,B01001000,B01001000,B01110000,B01001000,B01000100,B01000100,B01111100}, //B
{B00000000,B00011110,B00100000,B01000000,B01000000,B01000000,B00100000,B00011110},
{B00000000,B00111000,B00100100,B00100010,B00100010,B00100100,B00111000,B00000000},
{B00000000,B00111100,B00100000,B00111000,B00100000,B00100000,B00111100,B00000000},
{B00000000,B00111100,B00100000,B00111000,B00100000,B00100000,B00100000,B00000000},
{B00000000,B00111110,B00100000,B00100000,B00101110,B00100010,B00111110,B00000000}, //G
{B00000000,B00100100,B00100100,B00111100,B00100100,B00100100,B00100100,B00000000},
{B00000000,B00111000,B00010000,B00010000,B00010000,B00010000,B00111000,B00000000},
{B00000000,B00011100,B00001000,B00001000,B00001000,B00101000,B00111000,B00000000},
{B00000000,B00100100,B00101000,B00110000,B00101000,B00100100,B00100100,B00000000},
{B00000000,B00100000,B00100000,B00100000,B00100000,B00100000,B00111100,B00000000},//L
{B00000000,B00000000,B11000110,B10101010,B10010010,B10000010,B10000010,B00000000},//M
{B00000000,B00100010,B00110010,B00101010,B00100110,B00100010,B00000000,B00000000},
{B00000000,B00111100,B01000010,B01000010,B01000010,B01000010,B00111100,B00000000},
{B00000000,B00111000,B00100100,B00100100,B00111000,B00100000,B00100000,B00000000},
{B00000000,B00111100,B01000010,B01000010,B01000010,B01000110,B00111110,B00000001},
{B00000000,B00111000,B00100100,B00100100,B00111000,B00100100,B00100100,B00000000},
{B00000000,B00111100,B00100000,B00111100,B00000100,B00000100,B00111100,B00000000},
{B00000000,B01111100,B00010000,B00010000,B00010000,B00010000,B00010000,B00000000},
{B00000000,B01000010,B01000010,B01000010,B01000010,B00100100,B00011000,B00000000},
{B00000000,B00100010,B00100010,B00100010,B00010100,B00010100,B00001000,B00000000},
{B00000000,B10000010,B10010010,B01010100,B01010100,B00101000,B00000000,B00000000},
{B00000000,B01000010,B00100100,B00011000,B00011000,B00100100,B01000010,B00000000},
{B00000000,B01000100,B00101000,B00010000,B00010000,B00010000,B00010000,B00000000},
{B00000000,B00111100,B00000100,B00001000,B00010000,B00100000,B00111100,B00000000}}; //Z

int timeCount = 0;
int displayLength = 200;
//String w = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ";
String w = "SMCS ";
int letterCount = 0;
boolean solid = true;

void setup() 
{
    // Open serial port
    Serial.begin(9600);
    
    // Set all used pins to OUTPUT
    // This is very important! If the pins are set to input
    // the display will be very dim.
    for (byte i = 2; i <= 13; i++)
        pinMode(i, OUTPUT);
    pinMode(A0, OUTPUT);
    pinMode(A1, OUTPUT);
    pinMode(A2, OUTPUT);
    pinMode(A3, OUTPUT);
}

void loop() {
  // This could be rewritten to not use a delay, which would make it appear brighter
  delay(5);
  timeCount += 1;

  if(timeCount == displayLength){
    letterCount++;
    timeCount = 0;
    if(letterCount == w.length()){
      letterCount = 0;
      if(solid)
        solid = false;
      else
        solid = true;
    }
  }
  if(w.charAt(letterCount) == ' '){
    drawScreen(letters[0]); //blank
  }else{
    drawScreen(letters[w.charAt(letterCount)-63]);
  }


}
 void  drawScreen(byte buffer2[])
 { 
   // Turn on each row in series
    for (byte i = 0; i < 8; i++)        // count next row
     {
        digitalWrite(rows[i], HIGH);    //initiate whole row
        for (byte a = 0; a < 8; a++)    // count next row
        {
          // if You set (~buffer2[i] >> a) then You will have positive
          if(solid)
            digitalWrite(col[a], (buffer2[i] >> a) & 0x01); // initiate whole column
          else
            digitalWrite(col[a], (~buffer2[i] >> a) & 0x01); // initiate whole column
          
          delayMicroseconds(10);       // uncoment deley for diferent speed of display
          //delayMicroseconds(1000);
          //delay(10);
          //delay(100);
          
          digitalWrite(col[a], 1);      // reset whole column
        }
        digitalWrite(rows[i], LOW);     // reset whole row
        // otherwise last row will intersect with next row
    }
}
// 
  /* this is siplest resemplation how for loop is working with each row.
    digitalWrite(COL_1, (~b >> 0) & 0x01); // Get the 1st bit: 10000000
    digitalWrite(COL_2, (~b >> 1) & 0x01); // Get the 2nd bit: 01000000
    digitalWrite(COL_3, (~b >> 2) & 0x01); // Get the 3rd bit: 00100000
    digitalWrite(COL_4, (~b >> 3) & 0x01); // Get the 4th bit: 00010000
    digitalWrite(COL_5, (~b >> 4) & 0x01); // Get the 5th bit: 00001000
    digitalWrite(COL_6, (~b >> 5) & 0x01); // Get the 6th bit: 00000100
    digitalWrite(COL_7, (~b >> 6) & 0x01); // Get the 7th bit: 00000010
    digitalWrite(COL_8, (~b >> 7) & 0x01); // Get the 8th bit: 00000001
}*/
