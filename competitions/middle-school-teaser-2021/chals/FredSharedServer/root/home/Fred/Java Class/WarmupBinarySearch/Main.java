import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
class Main {
  public static void main(String[] args) throws Exception{
    ArrayList<String> list = new ArrayList<String>();
    URL wordList = new URL("https://github.com/dwyl/english-words/files/3086945/clean_words_alpha.txt");
    BufferedReader in = new BufferedReader(
                new InputStreamReader(
                wordList.openStream()));
    String inputLine;
    while ((inputLine = in.readLine()) != null)
        list.add(inputLine);
    in.close();
    System.out.println("The list size is: " + list.size());
    String searchTarget = "zebra";
    long start = System.currentTimeMillis();
    System.out.println(searchTarget + " is at position " + sequentialSearch(list,searchTarget));
    long end = System.currentTimeMillis();
    System.out.println("Sequential search took " + (end - start) + " milliseconds.");

    start = System.currentTimeMillis();
    System.out.println(searchTarget + " is at position " + binarySearch(list,searchTarget));
    end = System.currentTimeMillis();
    System.out.println("Binary search took " + (end - start) + " milliseconds.");
  }
  public static int sequentialSearch(ArrayList<String> words, String target){
    for(int i = 0; i < words.size(); i++){
      if(words.get(i).equals(target)){
        return i;
      }
    }
    return -1;
  }
    public static int binarySearch(ArrayList<String> words, String target){

    return -1;
  }
}