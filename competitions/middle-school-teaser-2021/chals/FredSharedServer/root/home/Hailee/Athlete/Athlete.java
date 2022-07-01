package Athlete;


public class Athlete implements Comparable<Athlete>{

	private String myLastName;
	private String myFirstName;
	
	public Athlete(){
		myLastName = "Woods";
		myFirstName = "Tiger";
	}
	public Athlete(String lastfirst){
		int comma = lastfirst.indexOf(',');
		myLastName = lastfirst.substring(0, comma);
		myFirstName = lastfirst.substring(comma + 1).trim();
	}
	public Athlete(String l, String f){
		myLastName = l;
		myFirstName = f;
	}
	public Athlete(Athlete other){
		myLastName = other.myLastName;
		myFirstName = other.myLastName;
	}
	public String toString(){
		return myFirstName + " " + myLastName;
	}

	public int compareTo(Athlete d) {
		return (myLastName+" "+myFirstName).compareTo(d.myLastName+" "+d.myFirstName);
	}


}
