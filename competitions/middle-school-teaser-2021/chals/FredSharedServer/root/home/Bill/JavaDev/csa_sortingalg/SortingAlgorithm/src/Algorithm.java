
public class Algorithm {
	public static Number[] number;
	public static void main(String[] args) {
		number = new Number[] { 
				new Number(9,0), 
				new Number(8,1), 
				new Number(7,2), 
				new Number(5,3), 
				new Number(4,4), 
				new Number(3,5), 
				new Number(6,6), 
				new Number(2,7), 
				new Number(1,8), 
				new Number(0,9)};
		// switch positions with a number if they are my position and they are less than I am
		for (int i = 0; i < 10; i++) {
			for (int o = 0; o < 10; o++) {
				if (number[o].value < number[i].value) {
					if (number[o].value == number[i].position) {
						int iPos = number[i].position;
						int oPos = number[o].position;
						number[o].position = iPos;
						number[i].position = oPos;
					}
				}
			}
		}
		for (int i = 0; i < 10; i++) {
			System.out.println("");
			System.out.println("");
			System.out.println(number[i].value);
			System.out.println(number[i].position);
		}
		
		
	}
}
