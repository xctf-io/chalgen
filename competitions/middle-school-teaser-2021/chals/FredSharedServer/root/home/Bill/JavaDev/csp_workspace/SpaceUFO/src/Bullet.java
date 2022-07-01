public class Bullet {
  public double x;
  public int y;
  public int speed;
  public Collider collider;
  public void Update(int fps) {
    x -= (double)speed / (double)fps;
    collider.Update((int)x,y);
  }
  Bullet(int _speed, int width, int height) {
    y = (int)Math.round(Math.random() * height);
    x = (double)width;
    speed = _speed;
    collider = new Collider((int)x,y,80,20);
  }
}