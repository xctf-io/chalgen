package Rational;

public class Rational {
	//fields
	private int a;
	private int b;
	//constructors
	public Rational(){
		a = 1;
		b = 1;
	}
	public Rational(int num, int den){
		a = num;
		if(den != 0){
			b = den;
		}else{
			throw new IllegalArgumentException("Cannot divide by 0.");
		}
	}
	public Rational(Rational other){
		a = other.a;
		b = other.b;
	}
	public void setValue(int num, int den){
		a = num;
		if(den != 0){
			b = den;
		}else{
			throw new IllegalArgumentException("Cannot divide by 0. (setValue method)");
		}	
	}
	public void simplify(){
		int g = gcf(a,b);
		a = a/g;
		b = b/g;
	}
	public Rational reciprocal(){
		return new Rational(b,a);
	}
	public Rational multiply(Rational other){
		Rational ans = new Rational(this.a * other.a, this.b * other.b);
		ans.simplify();
		return ans;
	}
	public Rational divide(Rational other){
		return this.multiply(other.reciprocal());
	}
	public String toString(){
		return "" + a + (b !=1 ? ("/" + b) : "");
	}
	public boolean equals(Object other){
		if(other.getClass()!= this.getClass()){
			return false;
		}
		Rational rat = (Rational)other;
		return a == rat.a && b == rat.b;
	}
	public Rational add(Rational other){
		return null;
	}
	public Rational subtract(Rational other){
		return null;
	}
	//since gcf is usable in other situations, it is made public
	//since gcf may be needed in situations without a Rational object, it is static
	public static int gcf(int a, int b){
		a = Math.abs(a);
		b = Math.abs(b);
		int counter = a;
		if(a > b)
			counter = b;
		while(!(a%counter == 0 && b%counter == 0))
			counter--;
		return counter;
	}

	
}
