package golpherQuiz;

public class Golfer implements Comparable<Golfer>{
	private String myLastName;
	private String myFirstName;
	private int myHandicap;
	private int id;
	
	private static int nextID = 1;
	
	public Golfer(){
		myLastName = "Woods";
		myFirstName = "Tiger";
		myHandicap = 0;
		id = nextID++;
	}
	public Golfer(String lastfirst, int h){
		myHandicap = h;
		int comma = lastfirst.indexOf(',');
		myLastName = lastfirst.substring(0, comma);
		myFirstName = lastfirst.substring(comma + 1).trim();
		id = nextID++;
	}
	public Golfer(String l, String f, int h){
		myLastName = l;
		myFirstName = f;
		myHandicap = h;
		id = nextID++;
	}
	public Golfer(Golfer other){
		myLastName = other.myLastName;
		myFirstName = other.myLastName;
		myHandicap = other.myHandicap;
		id = nextID++;
	}
	public String toString(){
		return myFirstName + " " + myLastName + 
				" has a handicap of " + myHandicap + ".";
	}
	public int getHandicap(){
		return myHandicap;
	}
	public void setHandicap(int h){
		myHandicap = h;
	}
	public int compareTo(Golfer obj) {
		Golfer d = (Golfer)obj;
		if(myHandicap != d.myHandicap)
			return myHandicap - d.myHandicap;
		return (myLastName+" " + myFirstName).compareTo(d.myLastName+" " + d.myFirstName);
	}


}
