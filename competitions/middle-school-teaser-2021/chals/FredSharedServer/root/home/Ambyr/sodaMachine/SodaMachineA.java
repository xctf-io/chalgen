package sodaMachine;

public class SodaMachineA {
	
	private static int nextID = 1;

	
	private int machineID;
	private int howManyKinds;
	
	//no-args constructor
	public SodaMachineA() {
		this(5);
		//machineID = nextID++;
		//howManyKinds = 5;
	}
	
	public SodaMachineA(int numOfKinds) {
		machineID =  nextID++;
		howManyKinds = numOfKinds;		
	}


	public String toString() {
		return "SodaMachine [machineID=" + machineID + ", howManyKinds=" + howManyKinds + "]";
	}
	
}
