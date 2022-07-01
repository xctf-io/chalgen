package kitKatObjects;

public class KitKat {
	//fields
	private int numberOfPieces;
	private String chocolateType;
	
	//constructors
	public KitKat(){
		numberOfPieces = 2;
		chocolateType = "milk";
	}
	public KitKat(int pieces, String choco) throws WhatAreYaNutsException{
		if(pieces < 1){
			throw new WhatAreYaNutsException("Must have at least 1 piece");
		}
		numberOfPieces = pieces;
		chocolateType = choco;
	}
	public KitKat(KitKat other){
		numberOfPieces = other.numberOfPieces;
		chocolateType = other.chocolateType;
	}
	public String giveMeABreak(){

		if(numberOfPieces == 0){
			throw new WhatAreYaNutsException("Nothing here to give you.");
		}
		numberOfPieces--;
		return "munch, munch";
	}
	@Override
	public String toString() {
		return "KitKat [numberOfPieces=" + numberOfPieces + ", chocolateType="
				+ chocolateType + "]";
	}
	
}
