package com.lieutenantjaku.testing.framework;

import java.util.LinkedList;

public class ArrayMethods {
	public int checkAmount(LinkedList list,Object searchFor) {
		int count=0;
		Object temp;
		for(int i=0; i<list.size();i++) {
			temp=list.get(i);
			if (temp.getClass()==searchFor.getClass()) {
				count++;
			}
		}
		return count;
	}
}
