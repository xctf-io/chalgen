import java.util.Scanner;
class Main {
  public static void main(String[] args) {
    String x = "Potato";
    System.out.println(testUnderstanding(x));
  }
    public static String testUnderstanding(String x) {
      String change = "yes";//This code declares and initializes some variables
      String repeatedWord = "L";
      System.out.println("");
      System.out.println("You will pick two numbers.  A random number will be picked out of those two numbers.  A word  you choose will be repeated that many times.");
      //This tells the user what the code does
      System.out.println("");//This formats the output
      Scanner numScan = new Scanner(System.in);
      System.out.print("Enter the minimum integer:    ");
      int num = numScan.nextInt();
      Scanner num2Scan = new Scanner(System.in);
      System.out.print("Enter the maximum integer:    ");
      int num2 = num2Scan.nextInt();
      System.out.println("");
      int num2New = num2 - num + 1;//This code finds the range using the maximum integer
      int randNum = (int)(Math.random()*num2New)+num;
      if(num > num2) {//This code tells the user if the minimum integer is greater than the maximum integer and it makes the random integer equal to the minimum integer
        System.out.println("Your minimum number was greater than your maximimum number.  ");
        System.out.println("");
        randNum = num;
      }
      int randNumForEnd = randNum;//This allows me to use the random integer after I change it to zero
      System.out.println("Your random number is " + randNum);System.out.println("");
      System.out.println("Would  you like to change the repeated word from " + x + "?");
      Scanner wantXScan = new Scanner(System.in);
      String wantX = wantXScan.nextLine();
      switch(wantX) {
        case "Yes":
        case "yes":
        //This allows the code to work if the user puts in a different yes
          System.out.print("What word do you want to have repeated instead:    ");
          Scanner repeatedWordScan = new Scanner(System.in);
          repeatedWord = new String(repeatedWordScan.nextLine());
          break;
        case "No":
        case "no":
          repeatedWord = new String(x);//It uses new string because strings are immutable
          break;
        case "MURPH":
        case "Murph":
        case "murph":
        //This code is there because I like the word murph
          System.out.println("MURPH");
          repeatedWord = new String("MURPH");
          randNum = 7;
          randNumForEnd = 7;
          break;
        default:
        //This code allows it to work if the user enters bad data
          System.out.println("Please say Yes or No.  The code will continue using " + x + ".");
          repeatedWord = new String(x);
          break;
      
      }
      System.out.println("");
      while(randNum > 0) {
        System.out.print(repeatedWord + " ");
        randNum--;//This prints the word I want as many times as randNum is equal to
      }
      System.out.println("");//The first line down is used because the repeated word doesnt print on a new line
      System.out.println("");
      if(randNumForEnd == 1) {//This if statement makes the output say "time" if the random number is 1
        return "The word " + repeatedWord + " was repeated " + randNumForEnd + " time.";
      }else{
        return "The word " + repeatedWord + " was repeated " + randNumForEnd + " times.";
      }
  }
}