package kitKatObjects;

public class KitKatApplication {

	public static void main(String[] args) {
		KitKat give = new KitKat();
		KitKat me = new KitKat(4, "milk");
		KitKat a = new KitKat(2, "white");
		KitKat brake = new KitKat(me); //no breaks except in switch statements!
		
		System.out.println(give + "\n" +
				me + "\n" +
				a + "\n" +
				brake + "\n");
		
		System.out.println(me.giveMeABreak());
		System.out.println(me);
		
		KitKat cheap = new KitKat(1, "milk");
		System.out.println(cheap.giveMeABreak());
		System.out.println(cheap.giveMeABreak());
	}
}
/*
KitKat [numberOfPieces=2, chocolateType=milk]
KitKat [numberOfPieces=4, chocolateType=milk]
KitKat [numberOfPieces=2, chocolateType=white]
KitKat [numberOfPieces=4, chocolateType=milk]

munch, munch
KitKat [numberOfPieces=3, chocolateType=milk]
munch, munch
Exception in thread "main" kitKatObjects.WhatAreYaNutsException: Nothing here to give you.
	at kitKatObjects.KitKat.giveMeABreak(KitKat.java:27)
	at kitKatObjects.KitKatApplication.main(KitKatApplication.java:21)
	
*/
