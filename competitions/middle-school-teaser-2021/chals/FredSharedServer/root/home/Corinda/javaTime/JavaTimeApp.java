package javaTime;

public class JavaTimeApp {
	public static void main(String[] args) {
		JavaTime jt = new JavaTime();
		System.out.println(jt.toString()+ " and " + jt.toAMPMString());
		jt.setTime(16,45);
		System.out.println(jt.toString()+ " and " + jt.toAMPMString());
		jt.setTime(26,10);
		System.out.println(jt.toString()+ " and " + jt.toAMPMString());
		jt.incrementMinute();
		System.out.println(jt.toString()+ " and " + jt.toAMPMString());
		jt.setTime(23,59);
		System.out.println(jt.toString()+ " and " + jt.toAMPMString());
		jt.incrementMinute();
		System.out.println(jt.toString()+ " and " + jt.toAMPMString());
		JavaTime jt2 = new JavaTime(jt);
		if(jt.equals(jt2)) {
			System.out.println(jt + " equals " + jt2);
		}else {
			System.out.println(jt + " does not equal " + jt2);
		}
	}
}
/* OUTPUT *****
0:0 and 0:0AM
16:45 and 4:45PM
16:45 and 4:45PM     //NOTE: Since the change was not legal, it seems to have not changed the value at all
16:46 and 4:46PM
23:59 and 11:59PM
0:0 and 0:0AM
0:0 does not equal 0:0
*/
//NOTE:  The very last line is incorrect...what might be wrong in the Object class?