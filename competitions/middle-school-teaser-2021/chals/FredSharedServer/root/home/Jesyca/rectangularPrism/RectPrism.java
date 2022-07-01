package rectangularPrism;
/** @author Mark Estep
 * @version 1.0
 * Date: 11/29/17
 * Demonstrates a simple Object Class
 */
public class RectPrism {
	private int width;
	private int height;
	private int depth;
	public RectPrism() {
		width = 1;
		height = 1;
		depth = 1;
	}
	public RectPrism(int w, int h, int d) {
		super();  //it's always here...usually not written!
		this.width = w;  //"this" is optional as well
		this.height = h;
		this.depth = d;
	}
	public RectPrism(RectPrism other) {
		//finish this
	}
	public int volume() {
		return width * height * depth;
	}
	public int areaFront() {
		return width * height;
	}
	public int areaBack() {
		return areaFront();
	}
	public int areaTop() {
		return width * depth;
	}
	public int areaBottom() {
		return areaTop();
	}
	public int areaLeftSide() {
		return height * depth;
	}
	public int areaRightSide() {
		return areaLeftSide();
	}
	public int getWidth() {
		return width;
	}
	public int getHeight() {
		return height;
	}
	public int getDepth() {
		return depth;
	}
	public void setWidth(int w) {
		this.width = w;
	}
	public void setHeight(int h) {
		this.height = h;
	}
	public void setDepth(int d) {
		this.depth = d;
	}
}
