package rectangularPrism;
/** @author Mark Estep
 * @version 1.0
 * Date: 11/29/17
 * Demonstrates an Application class for a simple Object.  (Driver class)
 */
public class RectangularPrismApp {

	public static void main(String[] args) {
		RectPrism box1 = new RectPrism();
		System.out.println(box1); //no toString() written...but it still compiles-- why?
		System.out.println(box1.volume());
		System.out.println(box1.areaBack());
		
		box1 = new RectPrism(3,1,2); //width, height, depth
		System.out.println(box1);
		System.out.println(box1.volume());
		System.out.println(box1.areaTop());
		System.out.println(box1.areaFront());
		
		box1.setHeight(4);
		System.out.println(box1);
		System.out.println(box1.volume());
		System.out.println(box1.areaBottom());
		System.out.println(box1.areaLeftSide());
	}

}
