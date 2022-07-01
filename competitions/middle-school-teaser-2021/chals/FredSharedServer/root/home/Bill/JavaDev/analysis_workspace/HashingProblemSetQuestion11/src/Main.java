import java.util.*;
import java.util.Map.Entry;
import java.io.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	public String mostFrequentWord(Scanner input) {
		Map<String, Integer> map = new HashMap<String, Integer>();
		while (input.hasNextLine()) {
			String line = input.nextLine();
			String[] words = line.split(" ");
			for (int i = 0; i < words.length; i++) {
				Integer thisCount = map.get(words[i]);
				if (thisCount == null) thisCount = 0;
				map.put(words[i], thisCount + 1);
			}
		}
		String topKey = "";
		Integer topValue = 0;
		for (Map.Entry<String, Integer> pair : map.entrySet()) {
		    if (pair.getValue() > topValue) {
		    	topValue = pair.getValue();
		    	topKey = pair.getKey();
		    }
		}
		return topKey;
	}

}
