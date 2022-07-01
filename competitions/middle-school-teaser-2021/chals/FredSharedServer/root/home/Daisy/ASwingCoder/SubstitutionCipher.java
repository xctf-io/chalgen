import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class SubstitutionCipher implements Codable{
  private String key;

  char[] upper = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                  'O','P','Q','R','S','T','U','V','W','X','Y','Z'};
  char[] lower = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                'o','p','q','r','s','t','u','v','w','x','y','z'};

  public SubstitutionCipher(String k){
    key = k;
  }
  
  public String encode(String plainText){
    String cipherText = "";
    for (int i=0; i<plainText.length(); i++) {
      if(Character.isUpperCase(plainText.charAt(i))){
        for (int x=0; x<upper.length; x++){
          if(upper[x] == plainText.charAt(i)){
            cipherText += key.substring(x,x+1);
          }
        }
      } else if(Character.isLowerCase(plainText.charAt(i))){
        for (int x=0; x<lower.length; x++){
          if(lower[x] == plainText.charAt(i)){
            cipherText += key.toLowerCase().substring(x,x+1);
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
          if(key.charAt(x) == cipherText.charAt(i)){
            plainText += upper[x];
          }
        }
      } else if(Character.isLowerCase(cipherText.charAt(i))){
        for (int x=0; x<lower.length; x++){
          if(key.toLowerCase().charAt(x) == cipherText.charAt(i)){
            plainText += lower[x];
          }
        }
      } else {
        plainText += cipherText.charAt(i);
      }
    }
    return plainText;
  }
}