//import System.*;
public class Player {
  public int x = 200;
  public int y = 0;
  public int vel = 1; // velocity
  public int gravity = 1; // gravity
  public int jumpForce = -10; // jumpForce
  public int width = 50;
  public Collider collider;

  public void Update() {
    vel += gravity;
    y = y + vel;
    collider.Update(x,y);
  }

  public void KeyPress() {
    vel = jumpForce;
  }

  // Instantiate a Player with variables
  Player(int _x, int _y, int _vel, int _gravity, int _jumpForce) {
    x = _x;
    y = _y;
    vel = _vel;
    gravity = _gravity;
    jumpForce = _jumpForce;
    collider = new Collider(_x, _y, width);
    System.out.println(collider);
  }

  // Override incase we want to use default variables
  Player() {
    collider = new Collider(x, y, width);
  }
}