import java.util.TreeMap;
import java.util.*;

class Main {
  public static void main(String[] args) {
    TreeMap<String, String> networkMap = new TreeMap<String, String>();
    for (int i = 0; i < 10; i++) {
      Scanner scanner = new Scanner(System.in);
      System.out.print("TV Channel? ");
      String c = scanner.nextLine();
      System.out.print("TV Show? ");
      String s = scanner.nextLine();
      networkMap.put(c,s); // maybe use put()
      System.out.println(networkMap);
    }
    ArrayList keys = new ArrayList(networkMap.keySet());
    Collections.sort(keys);
    System.out.println(keys);
    for (int i = 0; i < keys.size(); i++) {
      Object k = keys.get(i);
      System.out.println(k);
    }
  }
}