

public class GreetingApplication {

	public static void main(String[] args) {
		Greetable a = new SpanishSpeaker();
		Greetable b = new EnglishSpeaker();	
		Greetable c = new CoolEnglishSpeaker();
		
		greet(a);
		greet(b);
		greet(c);

	}
	public static void greet(Greetable greeter) {
		System.out.println(greeter.sayHello());
	}
}
