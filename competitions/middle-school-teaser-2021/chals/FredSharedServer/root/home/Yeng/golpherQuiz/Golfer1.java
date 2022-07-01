package golpherQuiz;

import Athlete.Athlete;

public class Golfer extends Athlete{
	private int myHandicap;
	
	public Golfer(){
		super();
		myHandicap = 0;
	}
	public Golfer(String lastfirst, int h){
		super(lastfirst);
		myHandicap = h;
	}
	public Golfer(String l, String f, int h){
		super(l,f);
		myHandicap = h;
	}
	public Golfer(Golfer other){
		super(other);
		myHandicap = other.myHandicap;
	}
	public String toString(){
		return super.toString() + 
				" has a handicap of " + myHandicap + ".";
	}
	public int getHandicap(){
		return myHandicap;
	}
	public void setHandicap(int h){
		myHandicap = h;
	}
	public int compareTo(Golfer d) {
		if(myHandicap != d.myHandicap)
			return myHandicap - d.myHandicap;
		return super.compareTo(d);
	}


}
