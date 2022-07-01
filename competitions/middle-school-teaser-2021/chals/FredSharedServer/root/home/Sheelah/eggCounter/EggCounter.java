package eggCounter;

/**
	* This class demonstrates a simple Java class that is not a "program class".
	* @author Mark Estep
	* @version 1.0
*/
public class EggCounter{
	//Data Members (Fields)******************************************* 
	private int myValue;
	//Constructors****************************************************
   /**
    * Default Constructor - sets counter to 0.
   */
   public EggCounter(){
      myValue = 0;
   }
   /**
    * Constructor - sets counter value to firstValue if it is a multiple of 12.
    * 	Otherwise, counter is set to 0.
    * @param firstValue - must be a multiple of 12 for counter to be set.
   */
   public EggCounter(int firstValue){
      if(firstValue % 12 != 0){
         System.out.println("I'm sorry, eggs only come in dozens!"
         	+ "\nThe value of your counter is 0.");
			myValue = 0;
		}else
		   myValue = firstValue;
	}
	//Accessors*******************************************************
   /**
    * This method returns the value of the counter.
    * @return myValue
   */
   public int getValue(){
      return myValue;
   }
   //Mutators********************************************************
   /**
    * This method adds 12 to the value of the counter.
   */
   public void buyEggs(){
      myValue+=12;
   }
   /**
    * This method subtracts 1 from the value of the counter if 1
    * is less than or equal to the value of the counter.  Otherwise, an error message appears on the 
    * screen and the value of the counter is not changed.
    * @param howMany - an integer value representing the number of eggs to be used.
   */
   public void useEgg(){
      if(myValue >= 1)
         myValue -= 1;
      else
         System.out.println("You don't have an egg!");
   }

}//end EggCounter class

   
