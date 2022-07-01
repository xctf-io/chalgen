import java.awt.*;
import java.awt.geom.Rectangle2D;

import javax.swing.*;
public class RectComponent extends JComponent {
  int width = 80;
  int height = 20;
  int x = 0;
  int y = 0;

  public void paintComponent(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    Rectangle box = new Rectangle(x, y, width, height);
    g2.draw(box);
  }
  public RectComponent(int _x, int _y, int _width, int _height) {
    width = _width;
    height = _height;
    x = _x;
    y = _y;
  }
}