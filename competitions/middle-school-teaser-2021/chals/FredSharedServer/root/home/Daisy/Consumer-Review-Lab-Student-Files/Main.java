
class Main {
  public static void main(String[] args) {

    String text = Review.textToString("WORK.txt"); 
    //converts from txt file to a string
    String text2 = Review.textToString("simpleReview.txt");
    String text3 = Review.textToString("26WestReview.txt");
    
    System.out.println(Review.totalSentiment(text));
    System.out.println(Review.totalSentiment(text2));
    System.out.println(Review.totalSentiment(text3));


  }
}