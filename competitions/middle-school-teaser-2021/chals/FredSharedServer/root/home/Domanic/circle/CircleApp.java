package circle;


public class CircleApp {
	/**
	 * with your table partner...
	 * 1.  Why should every class have a toString()
	 * 2.  What does a toString() return?
	 * 
	 * Compare and contrast     ==   and .equals()
	 * == --> compares primitives (what is on the stack)
	 * .equals --> compare Objects
	 * 
	 */
	public static void main(String[] args) {
		Circle c1 = new Circle();
		System.out.println(c1);
		Circle c2 = new Circle(5, 2, 3); 
		System.out.println(c2);
		Circle c3 = new Circle(c2);
		System.out.println(c3);
		
		System.out.println(c2.equals(c3));
		c3.setCenterX(3);
		System.out.println(c3);
		System.out.println(c2.equals(c3));
		
		System.out.println(c3.getArea());
		System.out.println(c3.getCircumference());
		
		System.out.println(c1.pointOnCircle(1,0));
		System.out.println(c1.pointOnCircle(1,1));
		
		System.out.println(c2.pointContainedInCircle(2,0));
		System.out.println(c2.pointContainedInCircle(2,9));
	}
}
/**
 * ****************OUTPUT********************************************
Circle [radius= 1.0, center at (0, 0)]
Circle [radius= 5.0, center at (2, 3)]
Circle [radius= 5.0, center at (2, 3)]
true
Circle [radius= 5.0, center at (3, 3)]
false
78.53981633974483
31.41592653589793
true
false
true
false
 ********************************************************************
 */
