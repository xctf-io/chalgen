package point;

public class PointApplication {
	public static void main(String[] args) {
		Point p1 = new Point();
		Point p2 = new Point(3,4);
		System.out.println("The distance from " + p1 + " to " 
				+ p2 + " is " + p1.distanceTo(p2) + ".");
		p1.setX(1);
		p2.setY(-2);
		System.out.println("The midpoint of" + p1 + " and " 
				+ p2 + " is " + p1.midpoint(p2) + ".");
	}
}
/**
The distance from (0, 0) to (3, 4) is 5.0.
The midpoint of(1, 0) and (3, -2) is (2, -1).
*/