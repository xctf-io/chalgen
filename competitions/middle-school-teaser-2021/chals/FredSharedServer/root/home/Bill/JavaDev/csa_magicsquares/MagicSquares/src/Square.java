import java.util.ArrayList;

/**
   A magic square is an n x n matrix which, if filled with numbers,
   the sum of the elements in each row, each column,
   and the two diagonal is the same value.
*/
public class Square
{
	public int[][] values;
	int x = 0;
	int y = 0;
   /**
      Construct a Square object.
   */
   public Square()
   {
       values = new int[4][4];
   }

   /**
      Add a number to the ArrayList of values.
      @param val the number to add
   */
   public void add(int val)
   {
       values[y][x] = val;
       System.out.println(y + ", " + x);
       
       x += 1;
       if (x == 4) {
    	   y += 1;
    	   x = 0;
       }
   }


   /**
      Determine if the square is a magic square.
      @return true if square is a magic square, false otherwise
   */
   public boolean isMagic()
   {
	  ArrayList sums = new ArrayList();
	  // Rows
      for (int y2 = 0; y2 < 4; y2++)
    	  sums.add(GetRowSum(y2));
      // Coloumns
      for (int x2 = 0; x2 < 4; x2++)
    	  sums.add(GetColumnSum(x2));
      // Diagonals
      sums.add(GetDiagonalSquaresSum());
      sums.add(GetDiagonalOtherSum());
      // Analyse
      int sum = (int)sums.get(0);
      System.out.print(sums);
      for (int i = 1; i < 10; i++) {
    	  if ((int)sums.get(i) != sum)
    		  return false;
      }
      return true;
      
   }
   public int GetRowSum(int y) {
	   int sum = 0;
	   for (int x2 = 0; x2 < 4; x2++) {
		   sum += values[y][x2];
	   }
	   return sum;
   }
   public int GetColumnSum(int x) {
	   int sum = 0;
	   for (int y2 = 0; y2 < 4; y2++) {
		   sum += values[y2][x];
	   }
	   return sum;
   }
   public int GetDiagonalSquaresSum() {
	   int sum = 0;
	   for (int x2 = 0; x2 < 4; x2++) {
		   for (int y2 = 0; y2 < 4; y2++) {
			   if (x2 == y2)
				   sum += values[y2][x2];
		   }
	   }
	   return sum;
   }
   public int GetDiagonalOtherSum() {
	   int sum = 0;
	   for (int x2 = 0; x2 < 4; x2++) {
		   for (int y2 = 0; y2 < 4; y2++) {
			   if ((x2 + 1) + (y2 + 1) == 5)
				   sum += values[y2][x2];
		   }
	   }
	   return sum;
   }
}
