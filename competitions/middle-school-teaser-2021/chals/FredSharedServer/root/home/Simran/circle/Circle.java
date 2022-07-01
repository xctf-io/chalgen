package circle;


public class Circle {
	private double myRadius;
	private int centerX;
	private int centerY;
	
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
	
	public boolean equals(Object other){
		if(!(other instanceof Circle) || other == null){
			return false;
		}
		Circle otherCircle = (Circle)other;
		return this.myRadius == otherCircle.myRadius && centerX == otherCircle.centerX  && centerY == otherCircle.centerY;
	}

	public Circle(double myRadius, int centerX, int centerY) {
		super();
		this.myRadius = myRadius;
		this.centerX = centerX;
		this.centerY = centerY;
	}
	public Circle(Circle c) {
		super();
		this.myRadius = c.myRadius;
		this.centerX = c.centerX;
		this.centerY = c.centerY;
	}
	public Circle(){
		myRadius = 1;
		centerX = 0;
		centerY = 0;
	}

	@Override
	public String toString() {
		return "Circle [radius= " + myRadius + ", center at (" + centerX
				+ ", " + centerY + ")]";
	}

	public double getMyRadius() {
		return myRadius;
	}

	public void setMyRadius(double myRadius) {
		this.myRadius = myRadius;
	}

	public int getCenterX() {
		return centerX;
	}

	public void setCenterX(int centerX) {
		this.centerX = centerX;
	}

	public int getCenterY() {
		return centerY;
	}

	public void setCenterY(int centerY) {
		this.centerY = centerY;
	}
	public double getArea(){
		return Math.PI * myRadius * myRadius;
	}
	public double getCircumference(){
		return 2 * Math.PI * myRadius;
	}
	public boolean pointOnCircle(int x, int y){
		return distance(centerX, centerY, x, y) == myRadius;
	}
	public boolean pointContainedInCircle(int x, int y){
		return distance(centerX, centerY, x, y) < myRadius;
	}
	public boolean overlaps(Circle other){
		return distance(centerX, other.centerX, centerY, other.centerY) <= myRadius + other.myRadius;
	}
	private double distance(int x1, int y1, int x2, int y2){
		return Math.sqrt(Math.pow(x1-x2,2) + Math.pow(y1-y2, 2));
	}
	
	
	
	

}
