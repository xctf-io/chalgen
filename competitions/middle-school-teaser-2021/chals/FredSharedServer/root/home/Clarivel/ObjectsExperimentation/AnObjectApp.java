package ObjectsExperimentation;

import java.util.Date;

public class AnObjectApp {

	public static void main(String[] args) {
		AnObject a = new AnObject("A");
		AnObject b = new AnObject("B");
		System.out.println("a is: "+ a);
		System.out.println("b is: "+ b);
		System.out.println();

		a.method(b);
		System.out.println();

		b.method(a);
		System.out.println();
		
		Date d = new Date(96,1,5);
		System.out.println(d);
		AnObject c = new AnObject("C", d);
		System.out.println(c);
		
		d.setMonth(7);
		System.out.println(c);
		
		String str1 = "Rational";
		String str2 = "ion";
		System.out.println(str1.indexOf(str2));
		//Create a memory diagram for the last 3 lines only...DURING the 
		//execution of the "indexOf()" method
	}
}