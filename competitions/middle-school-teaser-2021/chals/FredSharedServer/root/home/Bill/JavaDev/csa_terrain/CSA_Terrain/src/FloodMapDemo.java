public class FloodMapDemo
{
   public static void main(String[] args)
   {
      
      System.out.print("Enter height values:");
      double[][] heights = heightsGen(0,100);
      FloodMap floodMap = new FloodMap(heights);
      double min = floodMap.lowest();
      double max = floodMap.highest();
      floodMap.printFloodMap((max+min)/2);
   }
   public static double[][] heightsGen(double min, double max) {
	   double[][] heights = new double[10][10];
	   for (int x = 0; x < 10; x++) {
			for (int y = 0; y < 10; y++) {
				heights[y][x] = (Math.random() * max)+min;
			}
		}
	   return heights;
   }
}
