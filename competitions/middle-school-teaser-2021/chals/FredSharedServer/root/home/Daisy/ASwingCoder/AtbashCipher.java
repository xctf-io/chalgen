import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class AtbashCipher implements Codable{
  private String key;
  private String user;

  char[] upper = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                  'O','P','Q','R','S','T','U','V','W','X','Y','Z'};
  char[] lower = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                'o','p','q','r','s','t','u','v','w','x','y','z'};

  //user enters alphabet
  public AtbashCipher (String userInput){
    user = userInput;
    key = setKey(user);
  }

  //sets key to the reversed alphabet
  public String setKey(String userKey){
    String newKey = "";
    for (int i=userKey.length()-1; i>=0; i--){
      newKey += Character.toString(userKey.charAt(i));
    }
    key = newKey;
    return newKey;
  }

  public String encode(String plainText){
    String cipherText = "";
    for (int i=0; i<plainText.length(); i++) {
      if(Character.isUpperCase(plainText.charAt(i))){
        for (int x=0; x<user.length(); x++){
          if(user.charAt(x) == plainText.charAt(i)){
            cipherText += key.substring(x,x+1);
          }
        }
      } else if(Character.isLowerCase(plainText.charAt(i))){
        for (int x=0; x<user.length(); x++){
          if(user.toLowerCase().charAt(x) == plainText.charAt(i)){
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
        for (int x=0; x<key.length(); x++){
          if(key.charAt(x) == cipherText.charAt(i)){
            plainText += user.substring(x,x+1);
          }
        }
      } else if(Character.isLowerCase(cipherText.charAt(i))){
        for (int x=0; x<key.length(); x++){
          if(key.toLowerCase().charAt(x) == cipherText.charAt(i)){
            plainText += user.toLowerCase().substring(x,x+1);
          }
        }
      } else {
        plainText += cipherText.charAt(i);
      }
    }
    return plainText;
  }

}