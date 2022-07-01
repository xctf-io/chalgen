public class CaesarCipher implements Codable{
  private int shiftAmount;

  char[] upper = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                  'O','P','Q','R','S','T','U','V','W','X','Y','Z'};
  char[] lower = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                'o','p','q','r','s','t','u','v','w','x','y','z'};
  
  public CaesarCipher(int s){
    shiftAmount = s;
  }
  
  public void setShiftAmount(int shift){
    shiftAmount = shift;
  }
  
  public String encode(String plainText){
    String cipherText = "";
    for (int i=0; i<plainText.length(); i++) {
      if(Character.isUpperCase(plainText.charAt(i))){
        for (int x=0; x<upper.length; x++){
          if(upper[x] == plainText.charAt(i)){
            cipherText += upper[(x+shiftAmount)%26];
          }
        }
      } else if(Character.isLowerCase(plainText.charAt(i))){
        for (int x=0; x<lower.length; x++){
          if(lower[x] == plainText.charAt(i)){
            cipherText += lower[(x+shiftAmount)%26];
          }
        }
      } else {
        cipherText += plainText.charAt(i);
      }
    }
    return cipherText;
  }

  public String decode(String cipherText){
    String plainText = "";
    for (int i=0; i<cipherText.length(); i++) {
      if(Character.isUpperCase(cipherText.charAt(i))){
        for (int x=0; x<upper.length; x++){
          if(upper[x] == cipherText.charAt(i)){
            plainText += upper[((x-shiftAmount)+26)%26];
          }
        }
      } else if(Character.isLowerCase(cipherText.charAt(i))){
        for (int x=0; x<lower.length; x++){
          if(lower[x] == cipherText.charAt(i)){
            plainText += lower[((x-shiftAmount)+26)%26];
          }
        }
      } else {
        plainText += cipherText.charAt(i);
      }
    }
    return plainText;
  }
}
//if need to recompile file, go to shell -->
//javac CaesarCipher.java 