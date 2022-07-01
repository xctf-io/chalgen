package Rational;
public class RationalApp {
	public static void main(String[] args) {
		Rational r = new Rational();// 1/1
		System.out.println(r);
		Rational p = null;
		try{
			p = new Rational(2,0); 
		}catch(IllegalArgumentException e){
			System.out.println(e.getMessage());
		}
		p = new Rational(3,4);
		Rational q = new Rational(p);
		System.out.println("p = " + p + "\tq = " + q + "\tr = " + r);
		try {
			r.setValue(5, 0);
		}catch (IllegalArgumentException e) {
			System.out.println(e.getMessage());
		}
		try {
			r.setValue(2, 8);
		}catch (IllegalArgumentException e) {
			System.out.println(e.getMessage());
		}
		System.out.println("r = " + r);
		r.simplify();
		System.out.println("r = " + r);	
		
		r = new Rational(6,2);
		System.out.println("r = " + r);
		r.simplify();
		System.out.println("r = " + r);
	}
}
/*OUTPUT
1
Cannot divide by 0.
p = 3/4	q = 3/4	r = 1
Cannot divide by 0. (setValue method)
p = 3/4	q = 3/4	r = 2/8
p = 3/4	q = 3/4	r = 1/4
*/
