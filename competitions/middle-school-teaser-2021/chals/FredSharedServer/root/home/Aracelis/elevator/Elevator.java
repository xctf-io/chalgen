package elevator;

public class Elevator {
	//fields
	private static int nextID = 1;
	
	private int id;
	private int lowestFloor;
	private int highestFloor;
	private int currentFloor;
	
	public Elevator(int lf, int hf) {
		id = nextID++;
		lowestFloor = lf;
		highestFloor = hf;
		currentFloor = 1;
	}
	public Elevator(Elevator other) {
		id = nextID++;
		lowestFloor = other.lowestFloor;
		highestFloor = other.highestFloor;
		currentFloor = other.currentFloor;
	}
	
	public int gotoFloor(int floorRequested) {
		if(floorRequested < lowestFloor || floorRequested > highestFloor) {
			throw new IllegalArgumentException("Illegal floor requested.");
		}
		System.out.println("Moving from " + currentFloor + " to " + floorRequested);
		int distance = floorRequested - currentFloor;
		currentFloor = floorRequested;
		return distance;
	}
	
	public String toString() {
		return "Elevator #" + id + " - Currently at floor: " + currentFloor + ".";
	}
	
}
