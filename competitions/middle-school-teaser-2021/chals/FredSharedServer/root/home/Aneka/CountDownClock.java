import java.util.Date;


public class CountDownClock {
	private Date endDate;
	public CountDownClock(){
		endDate = new Date(108,5,2,11,0);
		System.out.println(endDate);
	}
	
	public void setEndTime(String y, String month, String d, 
			String h, String min){
		endDate = new Date(Integer.parseInt(y),
				Integer.parseInt(month),Integer.parseInt(d),
				Integer.parseInt(h),Integer.parseInt(min));
	}
	public String getRemaining(){
		String ans = "";
		long now = new Date().getTime();
		long end = endDate.getTime();
		long total =  (end - now) / 1000;
		long years = total / (365*24*60*60);
		total = total % (365*24*60*60);
		long days = total / (24*60*60);
		total = total % (24*60*60);
		long hours = total / (60*60);
		total = total % (60*60);
		long minutes = total / 60;
		long seconds = total % 60;
		
		ans = "" + (years>0?""+years+" year"+(years>1?"s\n":"\n"):"")+
				(days>=0?""+days+" day"+(days!=1?"s\n":"\n"):"")+
				(hours>=0?""+hours+" hour"+(hours!=1?"s\n":"\n"):"")+
				(minutes>=0?""+minutes+" minute"+(minutes!=1?"s\n":"\n"):"")+
				(seconds>=0?""+seconds+" second"+(seconds>1?"s\n":""):"");
			
		
		return ans;
	}
}
