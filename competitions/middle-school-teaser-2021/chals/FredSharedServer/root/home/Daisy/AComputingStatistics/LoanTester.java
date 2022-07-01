public class LoanTester {
   public static void main(String[] args) {
       Loan testOne = new Loan(12345, 280.00, "Japan", 5, 8);
       System.out.println(testOne);
       System.out.println("ID: 12345 loan amount: 280.0 country: Japan days to fund: 5 num lenders: 8");
       testOne.setID(54321);
      System.out.println(testOne.getID() + " == 54321");
       testOne.setLoanAmount(450.00);
       System.out.println(testOne.getLoanAmount() + " == 450.0");
       testOne.setCountry("USA");
       System.out.println(testOne.getCountry() + " == USA");
       testOne.setDaysToFund(12);
       System.out.println(testOne.getDaysToFund() + " == 12");
       testOne.setNumLenders(4);
      System.out.println(testOne.getNumLenders() + " == 4");
       System.out.println(testOne);
       System.out.println("ID: 54321 loan amount: 450.0 country: USA days to fund: 12 num lenders: 4");
   }
}