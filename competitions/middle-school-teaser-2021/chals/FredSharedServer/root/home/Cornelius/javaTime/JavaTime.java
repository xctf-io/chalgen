package javaTime;


public class JavaTime {
	//////////////////////////////////////////////////
	//           FIELDS
	//////////////////////////////////////////////////
	private int myHour;
	private int myMinute;
	//////////////////////////////////////////////////
	//           CONSTRUCTORS
	//////////////////////////////////////////////////
	public JavaTime(){
		//initialize all fields
		myHour = 0;
		myMinute = 0;
	}
	public JavaTime(int hour, int minute){
		//if time is valid - set the object's time
		//if invalid, set time to 0:00
		myHour = 0;
		myMinute = 0;
		if(!setTime(hour,minute))
			throw new IllegalArgumentException("Not a legal time!");
	}
	public JavaTime(JavaTime other){
		myHour = other.myHour;
		myMinute = other.myMinute;
	}
	///////////////////////////////////////////////////
	//             METHODS 
	//////////////////////////////////////////////////
	public String toString(){
		//converts time object to military time string
		return ""+myHour+":"+myMinute;
	}
	public String toAMPMString(){
		//converts time object to AM/PM string
		String amORpm =  "AM";
		if(myHour >= 12) {
			amORpm = "PM";
		}
		return "" + myHour%12 + ":" + myMinute + amORpm;
	}
	public void incrementMinute(){
		if(myMinute == 59){
			myMinute = 0;
			myHour++;
				if(myHour==24)
					myHour = 0;
		}else{
			myMinute++;	
		}
	}
	public boolean setTime(int hour, int minute){
		//returns false if invalid time and does not change
		//  the value of the time object (this)
		if(timeOK(hour, minute)){
			myHour = hour;
			myMinute = minute;
			return true;
		}else{
			return false;
		}		
	}
	private boolean timeOK(int hour, int minute){
		if(hour<0 || hour > 23)
			return false;
		if(minute < 0 || minute > 59)
			return false;
		return true;
	}

}
