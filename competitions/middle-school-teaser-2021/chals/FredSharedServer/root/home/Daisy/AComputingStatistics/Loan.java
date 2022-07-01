public class Loan{
  //instance variables
  private int ID;
  private double loanAmount;
  private String country;
  private int daysToFund;
  private int numLenders;

  //initialization constructor
  public Loan(int ID, double loanAmount, String country, int daysToFund, int numLenders) {
   this.ID = ID;
   this.loanAmount = loanAmount;
   this.country = country;
   this.daysToFund = daysToFund;
   this.numLenders = numLenders;
  }

  //accessor methods (getters)
  public int getID(){
    return ID;
  }
  public double getLoanAmount(){
    return loanAmount;
  }
  public String getCountry(){
    return country;
  }
  public int getDaysToFund(){
    return daysToFund;
  }
  public int getNumLenders(){
    return numLenders;
  }
  public String toString(){
    return "ID: " + getID() + " Loan amount: " + getLoanAmount() + " Country: " + getCountry() + " Days to Fund: " + getDaysToFund() + " Number of Lenders: " + getNumLenders();
  }

  //accessor methods (setters)
  public void setID(int newID){
    ID = newID;
  }
  public void setLoanAmount(double newLoanAmount){
    loanAmount = newLoanAmount;
  }
  public void setCountry(String newCountry){
    country = newCountry;
  }
  public void setDaysToFund(int newDaysToFund){
    daysToFund = newDaysToFund;
  }
  public void setNumLenders(int newNumLenders){
    numLenders = newNumLenders;
  }


  
}

