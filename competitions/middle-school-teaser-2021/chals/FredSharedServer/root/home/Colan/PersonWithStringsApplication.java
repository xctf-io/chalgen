import java.util.ArrayList;


public class PersonWithStringsApplication {
	public static void main(String[] args) {
		ArrayList<Person> personList1 = Person.makePersonList("First Last.txt");
		ArrayList<Person> personList2 = Person.makePersonList("First Middle Last.txt");
		ArrayList<Person> personList3 = Person.makePersonList("Last comma First.txt");
		
		System.out.println(personList1);
		System.out.println(personList2);
		System.out.println(personList3);		
	}
}
