int n = 10;    // default number
void setup() {
  Serial.begin(9600);
}

void loop() {
  while(Serial.available() == 0){  //method returns number of bytes arrived
    //empty loop to wait for bytes from computer to arrive (Serial port)
  }
  n = Serial.read();  //get the command from the computer

  //replace this loop with with communication back to computer 
  //(reply to the command) -- potentially lots of code!
  for(int count = 1; count <= n; count++){
    Serial.println(count);
  }
}

