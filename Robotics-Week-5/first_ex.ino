void setup() {
  pinMode(2, OUTPUT);
  // put your setup code here, to run once:

}
String letters[]={".-",
"-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",
".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};

void loop() {
//  digitalWrite(2, HIGH);
//  delay(1000);
//  digitalWrite(2, LOW);
//  delay(1000);
  String s = "absd";
  String morse = "";
  int lengthOfS = s.length();
  for(int i = 0; i<lengthOfS; i++)
  {
    char letter = s[i];
    int letterPosition = letter - 'a';
    morse += letters[letterPosition];//adding the translated into morse code letters 
    morse += '&';//between letter
 //  digitalWrite(2, HIGH);
//  delay(1000);
//  digitalWrite(2, LOW);
//  delay(1000);  
    
  }
  for(int i =0; i<morse.length(); i++){
    char character = s[i];
    if(character == '-'){
      digitalWrite(2, HIGH)
      delay(3000)
    }
    else if(charater == '.'){
      digitalWrite(2, HIGH)
      delay(1000)
    }
    else if(character == '&'){
      digitalWrite(2, LOW)
      delay(4000)
    }
    digitalWrite(2, LOW)
    delay(2000)
  }
  // put your main code here, to run repeatedly:
  
}
