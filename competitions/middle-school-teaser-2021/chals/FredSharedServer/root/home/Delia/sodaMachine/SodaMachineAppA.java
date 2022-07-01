package sodaMachine;

public class SodaMachineAppA {

	public static void main(String[] args) {
		SodaMachineA coke = new SodaMachineA(5);
		SodaMachineA pepsi = new SodaMachineA(7);
		SodaMachineA unkown = new SodaMachineA();
		SodaMachineA rc = new SodaMachineA(4);
		
		System.out.println(coke);
		System.out.println(pepsi);
		System.out.println(rc);
		System.out.println(unkown);

	}

}
