import java.util.*;
import java.io.*;
import java.text.*;

public class ComputingStatisticsRunner {
   public static void main(String[] args)  {
      // Specifies the data file to be used.
      String file = "data/kiva_loans.csv";
      
      // Creates an ArrayList to store the data and calls the readData() method. 
      ArrayList<Loan> list = readData(file);
      
      // Loop to print out the existing data to see how it is structured.
     // for(int i = 0; i < list.size(); i++) {
      //   System.out.println(list.get(i));
      //}  
      
      //Use this code to test the methods in the ComputingStatistics class
      ComputingStatistics analysis = new ComputingStatistics(list);
      System.out.println(analysis.totalAmount());
      System.out.println(analysis.avgLoan());       
      System.out.println(analysis.largestLoan());       
      System.out.println(analysis.smallestLoan());
      System.out.println(analysis.largestLoanCountry());
      System.out.println(analysis.smallestLoanCountry());
      System.out.println(analysis.avgDaysToFund());
      System.out.println(analysis.largestLoanKenya());
      System.out.println(analysis.avgLoanPhilippines());
      System.out.println(analysis.longestToFundCountry());
      System.out.println(analysis.variance());
      System.out.println(analysis.standardDeviation());
      System.out.println(analysis.empiricalRule());
   }
   
   
   /**
    * Reads in the provided file and creates an ArrayList of the data.
    * @param file the name of the text file containing the data.
    * @return the ArrayList containing the data from the text file.
    */
   public static ArrayList<Loan> readData(String file)  {
      // Scanner used to read in the data from the file.
      Scanner in = null;
      try{
        in = new Scanner(new File(file));
      }catch(FileNotFoundException e){
        System.out.println("File not found!");
        System.exit(1);
      }
      // ArrayList to store the data.
      ArrayList<Loan> list = new ArrayList<Loan>();
      // Read in the header line so it is not added to the ArrayLists.
      String header = in.nextLine();
      // Check to see if the file still has data to be read in.
      while(in.hasNextLine()) {
      
         SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
      
         // Read in the line of data and 
            // use a space as a delimiter to separate the different columns.
         String[] line = in.nextLine().split(",");
         
         // Local variable containing the ID.
         int ID = Integer.parseInt(line[0]);
         
         // Local variable containing the amount.
         int amount = Integer.parseInt(line[2]);
         
         // Local variable containing the country.
         String country = line[5];
         
         // Local variable containing the lenders.
         int lenders = Integer.parseInt(line[11]);
         
         // Local variable containing the difference in days.
         int differenceInDays = -1;
         
         try {
            Date postedDate = sdf.parse(line[8]);
        
            Date fundedDate = sdf.parse(line[9]);
            
            long differenceInTime = fundedDate.getTime() - postedDate.getTime(); 
                
            differenceInDays = (int)((differenceInTime / (1000 * 60 * 60 * 24)) % 365);       
         } 
         
        // Catch the Exception 
        catch (ParseException e) { 
            e.printStackTrace();
        }
        // Add the loan to the arraylist.
        list.add(new Loan(ID, amount, country, differenceInDays, lenders));         
        
      }
      // Return the completed ArrayLists.
      return list;
   }

}
