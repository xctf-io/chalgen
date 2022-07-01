package golpherQuiz;

public class GolferApplication {
	public static void main(String[] args) {
		Golfer a = new Golfer();
		Golfer b = new Golfer("Palmer, Arnold", 2);
		Golfer c = new Golfer("Sorenstam", "Annika", 1);
		Golfer d = new Golfer(c);
		
		
		System.out.println(a); 
		//"Tiger Woods has a handicap of 0."
		System.out.println(b.getHandicap());
		//"2"
		b.setHandicap(4);
		System.out.println(b.getHandicap());
		//"4"
		System.out.println(a.compareTo(b));
		//Compares the handicap of the golfers
	}
}
/*
Tiger Woods has a handicap of 0.
2
4
-4
*/