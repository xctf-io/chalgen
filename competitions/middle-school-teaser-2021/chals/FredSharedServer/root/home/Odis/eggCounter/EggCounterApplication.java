package eggCounter;

/*	Driver Program for EggCounter Class
*	GOALS:
*		-creating class objects (instances of the class) using constructors
*		-using object accessors to retrieve object attributes (usually fields)
*		-using object mutators to change the value of object attributes
*/		

import java.util.Scanner;
public class EggCounterApplication {
    private static final Scanner Keyboard = new Scanner(System.in);
	private static int ShowMenu(){
	   System.out.print("Please choose:"
	   	+"\n\t1.  Buy Eggs (one dozen)"
	   	+"\n\t2.  Use Eggs (in any number)"
	   	+"\n\t3.  Quit"
        +"\nCHOICE: ");
	   return Keyboard.nextInt();

	}
	public static void main(String args[]) {
        System.out.print("With how many eggs are you beginning? ");
	    int startValue = Keyboard.nextInt();
		EggCounter myEggs = new EggCounter(startValue);
		int choice;
		do{
			choice = ShowMenu();
			switch(choice){
			   case 1: myEggs.buyEggs();
			           break;
			   case 2: System.out.print("How many eggs are you using?");
                       int numOfEggs = Keyboard.nextInt();
                       for(int i = 1; i <= numOfEggs; i++)
			           		myEggs.useEgg();
			           break;
			   case 3: System.out.println("Thank you for using Eggcounter!");
			           break;
			   default: System.out.println("Please choose 1-3 only.");
		   }
		   System.out.println("You have "+myEggs.getValue()+" eggs.");
		}while(choice!=3);

	}
}
