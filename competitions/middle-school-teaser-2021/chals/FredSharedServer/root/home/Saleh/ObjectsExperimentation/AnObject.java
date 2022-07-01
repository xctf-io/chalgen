package ObjectsExperimentation;

import java.util.Date;

public class AnObject {
	private String myID;
	private Date dateField;

	public AnObject(String name) {
		myID = name;
	}
	public AnObject(String name, Date birth) {
		this(name);
		dateField = birth;
	}
	public String toString() {
		return super.toString() + ": " + myID + " - " + dateField;
	}
	public void method(AnObject other) {
		System.out.println("this is " + this);
		System.out.println("other is: "+ other);
	}
}