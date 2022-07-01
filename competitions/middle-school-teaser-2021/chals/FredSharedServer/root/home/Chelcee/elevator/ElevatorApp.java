package elevator;

public class ElevatorApp {

	public static void main(String[] args) {
		Elevator e = new Elevator(-2,5);
		
		//e.gotoFloor(3);
		//e.gotoFloor(5);
		//e.gotoFloor(-1);
		
		Elevator f = new Elevator(e);
		System.out.println(f);  //e.toString()
		
		e.gotoFloor(4);
		f.gotoFloor(2);
		
		System.out.println(e);
		System.out.println(f);
		
		
	}

}
