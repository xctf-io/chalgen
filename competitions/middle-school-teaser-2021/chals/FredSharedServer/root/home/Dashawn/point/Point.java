package point;

public class Point {
	//Fields
	private int x;
	private int y;
	
	//Constructors
	public Point() {
		x = 0;
		y = 0;
	}
	public Point(int a, int b) {
		x = a;
		y = b;
	}
	public Point(Point other) {
		x = other.x;
		y = other.y;
	}
	//Method(s) called explicitly
	public double distanceTo(Point other) {
		return Math.sqrt(Math.pow(x - other.x, 2) + Math.pow(y - other.y, 2));
	}
	public Point midpoint(Point other) {
		return  new Point((x + other.x)/ 2, (y + other.y)/2);
	}
	public void setX(int a) {
		x = a;
	}
	public void setY(int a) {
		y = a;
	}
	//Method(s) called implicitly
	public String toString() {
		return "(" + x + ", " + y + ")";
	}
	//Other required Method(s)
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Point other = (Point) obj;
		if (x != other.x)
			return false;
		if (y != other.y)
			return false;
		return true;
	}
	
}
