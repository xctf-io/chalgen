import java.util.Scanner;
import java.io.File;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Random;
import java.io.*;

/**
 * Class that contains helper methods for the Review Lab
 * (method removePunctuation() was added from teacher code)
 **/
public class Review {
  
  private static HashMap<String, Double> sentiment = new HashMap<String, Double>();
  private static ArrayList<String> posAdjectives = new ArrayList<String>();
  private static ArrayList<String> negAdjectives = new ArrayList<String>();
 
  
  private static final String SPACE = " ";
  
  static{
    try {
      Scanner input = new Scanner(new File("cleanSentiment.csv"));
      while(input.hasNextLine()){
        String[] temp = input.nextLine().split(",");
        sentiment.put(temp[0],Double.parseDouble(temp[1]));
        //System.out.println("added "+ temp[0]+", "+temp[1]);
      }
      input.close();
    }
    catch(Exception e){
      System.out.println("Error reading or parsing cleanSentiment.csv");
    }
  
  
  //read in the positive adjectives in postiveAdjectives.txt
     try {
      Scanner input = new Scanner(new File("positiveAdjectives.txt"));
      while(input.hasNextLine()){
        String temp = input.nextLine().trim();
      //  System.out.println(temp);
        posAdjectives.add(temp);
      }
      input.close();
    }
    catch(Exception e){
      System.out.println("Error reading or parsing postitiveAdjectives.txt\n" + e);
    }   
 
  //read in the negative adjectives in negativeAdjectives.txt
     try {
      Scanner input = new Scanner(new File("negativeAdjectives.txt"));
      while(input.hasNextLine()){
        negAdjectives.add(input.nextLine().trim());
      }
      input.close();
    }
    catch(Exception e){
      System.out.println("Error reading or parsing negativeAdjectives.txt");
    }   
  }
  
  /** 
   * returns a string containing all of the text in fileName (including punctuation), 
   * with words separated by a single space 
   */
  public static String textToString( String fileName )
  {  
    String temp = "";
    try {
      Scanner input = new Scanner(new File(fileName));
      
      //add 'words' in the file to the string, separated by a single space
      while(input.hasNext()){
        temp = temp + input.next() + " ";
      }
      input.close();
      
    }
    catch(Exception e){
      System.out.println("Unable to locate " + fileName);
    }
    //make sure to remove any additional space that may have been added at the end of the string.
    return temp.trim();
  }
  
  /**
   * @returns the sentiment value of word as a number between -1 (very negative) to 1 (very positive sentiment) 
   */
  public static double sentimentVal( String word )
  {
    try
    {
      return sentiment.get(word.toLowerCase());
    }
    catch(Exception e)
    {
      return 0;
    }
  }
  
  /**
   * Returns the ending punctuation of a string, or the empty string if there is none 
   */
  public static String getPunctuation( String word )
  { 
    String punc = "";
    for(int i=word.length()-1; i >= 0; i--){
      if(!Character.isLetterOrDigit(word.charAt(i))){
        punc = punc + word.charAt(i);
      } else {
        return punc;
      }
    }
    return punc;
  }
  
  /**
   * Returns the word after removing any beginning or ending punctuation
   */
  public static String removePunctuation( String word )
  {
    while(word.length() > 0 && !Character.isAlphabetic(word.charAt(0)))
    {
      word = word.substring(1);
    }
    while(word.length() > 0 && !Character.isAlphabetic(word.charAt(word.length()-1)))
    {
      word = word.substring(0, word.length()-1);
    }
    
    return word;
  }
  
  /** 
   * Randomly picks a positive adjective from the positiveAdjectives.txt file and returns it.
   */
  public static String randomPositiveAdj()
  {
    int index = (int)(Math.random() * posAdjectives.size());
    return posAdjectives.get(index);
  }
  
  /** 
   * Randomly picks a negative adjective from the negativeAdjectives.txt file and returns it.
   */
  public static String randomNegativeAdj()
  {
    int index = (int)(Math.random() * negAdjectives.size());
    return negAdjectives.get(index);
    
  }
  
  /** 
   * Randomly picks a positive or negative adjective and returns it.
   */
  public static String randomAdjective()
  {
    boolean positive = Math.random() < .5;
    if(positive){
      return randomPositiveAdj();
    } else {
      return randomNegativeAdj();
    }
  }

/** Activity 2: totalSentiment()
  * Write the code to total up the sentimentVals of each word in a review.
 */
  public static double totalSentiment(String fileName)
  {
    double sentimentTotal = 0.0;
    
    String [] myStringArray = fileName.split("[^a-zA-Z0-9']");
    for(int i = 0; i < myStringArray.length ; i++){
      sentimentTotal = sentimentTotal + sentimentVal(myStringArray[i]);
    }
   
   return sentimentTotal; 
  }


  /** Activity 2 starRating method
     Write the starRating method here which returns the number of stars for the review based on its totalSentiment.
  */
  public static int starRating(String fileName)
  {
    double total = totalSentiment(fileName);
    int stars = 0; 

    if (total <= 0){
      stars = 1;
    }
    else if (total > 0 && total <= 10 ){
      stars = 2; 
    }
    else if(total > 10 && total <= 20){
      stars = 3;
    }
    else if(total > 20 && total <= 30){
      stars = 4; 
    }
    else{
      stars = 5; 
    }

    // return number of stars
    return stars; 
  }


public static String fakeReview(String fileName){

  int astIndex = fileName.indexOf("*") ;
  int spaceIndex = fileName.indexOf(" ", astIndex);
  String replace = "";
  while(astIndex > -1){
   if(spaceIndex == -1){
     spaceIndex = fileName.length();
   }
    replace = fileName.substring(astIndex, spaceIndex);
    if(getPunctuation(replace).length() > 0){
      replace = fileName.substring(astIndex, spaceIndex -1);
    }

    fileName = fileName.replace(replace, randomAdjective());
    astIndex = fileName.indexOf("*", astIndex + 1);
    spaceIndex = fileName.indexOf(" ", astIndex);
  }

  return fileName; 
  }

public static String fakeReview2(String fileName){

  int astIndex = fileName.indexOf("*") ;
  int spaceIndex = fileName.indexOf(" ", astIndex);
  String replace = "";
  while(astIndex > -1){
   if(spaceIndex == -1){
     spaceIndex = fileName.length();
   }
    replace = fileName.substring(astIndex , spaceIndex);
    if(getPunctuation(replace).length() > 0){
      replace = fileName.substring(astIndex, spaceIndex -1);
    }
    if(totalSentiment(fileName) > 0.0){
      if(!(sentimentVal(removePunctuation(replace)) > 0.0)){
        fileName = fileName.replace(replace, randomPositiveAdj());
      }else{
        String word = replace; 
        word = replace.substring(1);
        fileName = fileName.replace(replace,word);
      }
    }
    else if(totalSentiment(fileName) < 0.0){
      if(!(sentimentVal(removePunctuation(replace)) < 0.0)){
        fileName = fileName.replace(replace,randomNegativeAdj());
      }else{
        String word = replace; 
        word = replace.substring(1);
        fileName = fileName.replace(replace,word);
      }
    }
    astIndex = fileName.indexOf("*", astIndex + 1);
    spaceIndex = fileName.indexOf(" ", astIndex);
  }

  return fileName; 
  }
}
