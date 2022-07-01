
public class FloodMap {
	double[][] heights;
	public FloodMap(double[][] _heights) {
		heights = _heights;
	}
	public void printFloodMap(double waterLevel) {
		for (int x = 0; x < 10; x++) {
			for (int y = 0; y < 10; y++) {
				if(heights[y][x] < waterLevel) {
					System.out.print("F");
				} else {
					System.out.print(" ");
				}
			}
			System.out.println();
		}
	}
	public double lowest() {
		double lowest = 1000.0;
		for (int x = 0; x < 10; x++) {
			for (int y = 0; y < 10; y++) {
				if (heights[y][x] < lowest)
					lowest = heights[y][x];
			}
		}
		return lowest;
	}
	public double highest() {
		double highest = 0;
		for (int x = 0; x < 10; x++) {
			for (int y = 0; y < 10; y++) {
				if (heights[y][x] > highest)
					highest = heights[y][x];
			}
		}
		return highest;
	}
}
