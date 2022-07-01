import java.util.ArrayList;

public class ComputingStatistics {
   //The ArrayList containing all of the loan data.
   private ArrayList<Loan> data;
   
   //Creates a new ComputingStatistics object with an empty ArrayList
   public ComputingStatistics() {
      data = new ArrayList<Loan>();
   }
   
   // Creates a new ComputingStatistics object with the data passed in
   public ComputingStatistics(ArrayList<Loan> d) {
      data = d;
   }
   
   /*Calclates the total amount funded from all of the loans in the file.
    * @return the total loan amount.
    */
   public double totalAmount() {
      double amount = 0.0;
      for(int i = 0; i < data.size(); i++) {
         amount = amount + data.get(i).getLoanAmount();
      }
      return amount;
   }

   public double avgLoan(){
      return this.totalAmount()/data.size();
   }

   public double largestLoan(){
     double largestSoFar = Integer.MIN_VALUE;
     for (int i=0; i<data.size(); i++){
       if (data.get(i).getLoanAmount() > largestSoFar){
         largestSoFar = data.get(i).getLoanAmount();
       }
     }
     return largestSoFar;    
   }

   public double smallestLoan(){
     double smallestSoFar = Integer.MAX_VALUE;
     for (int i=0; i<data.size(); i++){
       if (data.get(i).getLoanAmount() < smallestSoFar){
         smallestSoFar = data.get(i).getLoanAmount();
       }
     }
     return smallestSoFar;    
   }

   public String largestLoanCountry(){
     String country = "";
     double largest = this.largestLoan();
     for(int i=0; i<data.size(); i++){
       if (data.get(i).getLoanAmount() == largest){
         country = data.get(i).getCountry();
       }
     }
     return country;
   }

   public String smallestLoanCountry(){
     double smallest = this.smallestLoan();
     for(int i=0; i<data.size(); i++){
       if (data.get(i).getLoanAmount() == smallest){
         return data.get(i).getCountry();
       }
     }
     return null; //this won’t ever happen but java requires there should be a return statement
   } 

    //without using smllestLoan() method
    /*public String smallestLoanCountry(){
      String country = "";
      double smallestSoFar = Integer.MAX_VALUE;
      for (int i=0; i<data.size(); i++){
        if (data.get(i).getLoanAmount() < smallestSoFar){
          smallestSoFar = data.get(i).getLoanAmount();
          country = data.get(i).getCountry();
        }
      }
      return country;
    } */

   public double avgDaysToFund(){
     double total = 0.0;
     for (int i=0; i<data.size(); i++){
       total += data.get(i).getDaysToFund();
     }
     return total/data.size();
   }

   public double largestLoanKenya(){
     double largestSoFar = Integer.MIN_VALUE;     
     for (int i=0; i<data.size(); i++){
      if (data.get(i).getCountry().equals("Kenya")){
        if(data.get(i).getLoanAmount() > largestSoFar){
          largestSoFar = data.get(i).getLoanAmount();
        }
      }
     }
     return largestSoFar;
   }

   public double avgLoanPhilippines(){
     double total = 0.0;
     double count = 0.0;
     for (int i=0; i<data.size(); i++){
      if (data.get(i).getCountry().equals("Philippines")){
        total += data.get(i).getLoanAmount();
        count++;
      }
     }
     return total/count;
   }

   public String longestToFundCountry(){
     double longestSoFar = Integer.MIN_VALUE;
     int index = 0;
     for (int i=0; i<data.size(); i++){
       if (data.get(i).getDaysToFund() > longestSoFar){
         longestSoFar = data.get(i).getDaysToFund();
         index = i;
       }
     }
     return data.get(index).getCountry();
   }

   public String mostLoansFunded(){
     int k = 0;
     int e = 0;
     String country = "";
     for (int i=0; i<data.size(); i++){
       if(data.get(i).getCountry().equals("Kenya")){
         k++;
       }
       if(data.get(i).getCountry().equals("El Salvador")){
         e++;
       }
     }
     
     if (k>e){
       country = "Kenya";
     } else {
       country = "El Salvador";
     }

     return country;
   }

   public double variance(){
     double total = 0.0;
     double avg = this.avgLoan();
     for (int i=0; i<data.size(); i++){
       double n = data.get(i).getLoanAmount() - avg;
       total += Math.pow(n, 2);
     }
     return total/data.size();
   }

   public double standardDeviation(){
     return Math.sqrt(this.variance());
   }

   public boolean empiricalRule(){
     double count = 0.0;
     double lower = this.avgLoan() - this.standardDeviation();
     double higher =  this.avgLoan() + this.standardDeviation();
     for(int i=0; i<data.size(); i++){
       if(data.get(i).getLoanAmount()<higher && data.get(i).getLoanAmount()>lower){
         count++;
       }
     }
     if(count/data.size()*100 >= 68.0){
       return true;
     }
     return false;
   }


}