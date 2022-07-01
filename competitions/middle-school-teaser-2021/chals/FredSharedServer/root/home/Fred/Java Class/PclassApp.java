
public class PclassApp {
	public static void main(String[] args) {
		Pclass obj1 = new Pclass(4);
		Pclass obj2 = new Pclass();
		//Pclass obj3 = new Pclass(obj1);
		System.out.println(Pclass.puSt);
		//System.out.println(Pclass.piSt);
		//System.out.println(Pclass.getNum2());
		System.out.println(obj1.getNum2());
		System.out.println(obj1.getNum());	
		System.out.println(Pclass.getNum());
		System.out.println(obj1.changeIt(7));

		//System.out.println(Pclass.changeIt(5));
		System.out.println(obj1);
		//System.out.println(obj1.pi);
		System.out.println(obj1.pub);
		//System.out.println(obj1.piSt);
		System.out.println(obj1.puSt);
		//System.out.println(Pclass.pi);
		//System.out.println(Pclass.pub);
		//System.out.println(Pclass.piSt);
		System.out.println(Pclass.puSt);
		System.out.println(obj1.getNum());
		System.out.println(obj1.getNum2());
		System.out.println(Pclass.getNum());
		//System.out.println(Pclass.getNum2());	
	}
}
