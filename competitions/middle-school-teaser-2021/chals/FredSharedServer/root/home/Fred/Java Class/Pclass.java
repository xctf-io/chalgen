
public class Pclass {

	private static int piSt = 0;
	public static int puSt = 10;
	
	private int pi;
	public int pub;
	
	public Pclass(){
		pi = 3;
		pub = 6;
	}
	public Pclass(int x){
		pi = x;
		pub = 10;
	}
	public static int getNum(){
		return piSt;
	}
	public int getNum2(){
		return pi;
	}
	public int changeIt(int a){
		int temp = pub;
		pub = pi;
		pi = a;
		return temp;
	}
}
