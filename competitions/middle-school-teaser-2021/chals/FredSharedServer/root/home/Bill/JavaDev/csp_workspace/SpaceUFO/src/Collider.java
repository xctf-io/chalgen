public class Collider {
  public int x;
  public int y;
  public int sizeX;
  public int sizeY;
  public Collider(int _x, int _y, int _size) {
    x = _x;
    y = _y;
    sizeX = sizeY = _size;
  }
  public Collider(int _x, int _y, int _sizeX, int _sizeY) {
    x = _x;
    y = _y;
    sizeX = _sizeX;
    sizeY = _sizeY;
  }
  public void Update(int _x, int _y) {
    x = _x;
    y = _y;
  }
  public boolean IsCollidingWith(Collider other) {
    return (this.x > other.x && this.x < other.x + other.sizeX
    && this.y > other.y && this.y < other.y + other.sizeY);
  }
}