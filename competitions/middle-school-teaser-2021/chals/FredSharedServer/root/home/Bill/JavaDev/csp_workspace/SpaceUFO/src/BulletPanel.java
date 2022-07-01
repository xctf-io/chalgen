import java.awt.*;
import java.awt.event.*;
import java.awt.geom.Rectangle2D;
import java.util.ArrayList;
import javax.swing.*;
public class BulletPanel extends JPanel {
  ArrayList<Bullet> bullets;
  Player player;
  public void paintComponent(Graphics g) {
      super.paintComponent(g);
      Graphics2D g2 = (Graphics2D) g;
      for (int i = 0; i < bullets.size(); i++) {
        g2.draw (
          new Rectangle((int)bullets.get(i).x,(int)bullets.get(i).y,50,20)
        );
      }
      g2.draw(new Rectangle((int)player.x, (int)player.y, (int)player.width, (int)player.width));

  }
  public BulletPanel(ArrayList<Bullet> _bullets, Player _player) {
    bullets = _bullets;
    player = _player;
  }
  public void Update(ArrayList<Bullet> _bullets, Player _player) {
    bullets = _bullets;
    player = _player;
  }
}