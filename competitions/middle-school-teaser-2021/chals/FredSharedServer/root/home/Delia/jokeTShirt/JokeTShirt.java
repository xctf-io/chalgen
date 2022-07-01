package jokeTShirt;

public class JokeTShirt {
	private String subject;
	private String size;
	private String joke;
	
	public JokeTShirt() {
		this("CS","XL","");
	}
	
	public JokeTShirt(String sub, String s, String j) {
		subject = sub;
		size = s;
		joke = j;
	}
}
