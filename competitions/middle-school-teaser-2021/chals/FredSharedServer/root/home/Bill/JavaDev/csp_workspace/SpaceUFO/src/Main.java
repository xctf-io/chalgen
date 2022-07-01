import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
import java.util.ArrayList;
// import java.util.concurrent.*;

public class Main {
  static JFrame frame;
  static BulletPanel bp; // Bullet Panel
  static Component component;
  static JPanel cp; // Click Panel
  static JButton click;
  static int screenWidth = 720;
  static int screenHeight = 480;
  static int fps = 60;
  static ArrayList<Bullet> bullets;
  static double bulletTimer = 0.0;
  static double bulletCooldown = 0.3;
  static double secondsSinceStart = 0;
  static boolean isGameOver = false;
  static Player player;
  static Component pComponent;
  static MouseComponent mouseComponent; 
  public static void print(String string) {
	  System.out.println(string);
  }
  public static void main(String[] args) {
    Start();

    while (true) {
      if (!isGameOver) {
        Update();
      }

      try
      {
          secondsSinceStart += (double)1/(double)fps;
          Thread.sleep((int)(1000 / fps));
      }
      catch(InterruptedException ex)
      {
          Thread.currentThread().interrupt();
          System.out.println("Interrupted: ERROR Main");
      }
    }
  }
  public static void Start() {
    // Instantiate JFrame
    frame = new JFrame();
    frame.setSize(screenWidth, screenHeight);
    
    cp = new JPanel(); // Click Panel
    // Instantiate Click
    click = new JButton(" Jump ");
    // Boundaries
    click.setBounds((screenWidth / 2) - (100/2), screenHeight - 60, 150, 25);
    // Listener
    click.addActionListener(new ActionListener() {
      @Override
      public void actionPerformed(ActionEvent e) {
        // FUNCTION()
      }
    });
    cp.add(click);
    frame.add(cp);

   

    player = new Player();
    pComponent = frame.add(new RectComponent((int)player.x, (int)player.y, player.width, player.width));
    
    bullets = new ArrayList<Bullet>();
    bp = new BulletPanel(bullets, player);
    component = frame.add(bp);

    mouseComponent = new MouseComponent();
    frame.add(mouseComponent);
    frame.addMouseListener((MouseListener) mouseComponent);


    
  }
  public static void Update() {
    // Adding bullets to our list every few seconds
    if (bulletTimer <= 0) {
      bullets.add(new Bullet(500, screenWidth - 100, screenHeight));
      bulletTimer = bulletCooldown;
      System.out.println(" New Bullet ");
    }
    
    // Player
    
    if(mouseComponent.IsMouseClicked()) {
      player.KeyPress();
    }
    player.Update();

    ManageBullets();
    
    
    frame.remove(pComponent);
    pComponent = frame.add(new RectComponent((int)player.x, (int)player.y, player.width, player.width));
    
    
    // Drawing bullets
    bp.Update(bullets, player);
    frame.remove(bp);
    bp = new BulletPanel(bullets, player);
    frame.add(bp, BorderLayout.CENTER);

    // Revalidate frame to cause it to layout the new panel correctly.
    frame.revalidate();
    //f.show();
    bp.setVisible(true);
    frame.setVisible(true);
  }
  public static void ManageBullets() {
	  bulletTimer = bulletTimer - ((double)1/(double)fps);
	  for (int i = 0; i < bullets.size(); i++) {
		  bullets.get(i).Update(fps);
		  if (bullets.get(i).x < -100) {
			  bullets.remove(i);
		  }
		  boolean isColliding = bullets.get(i).collider.IsCollidingWith(player.collider);
		  if (isColliding && !isGameOver) {
			  EndGame();
		  }
	  }
  }
  public static void EndGame() {
    isGameOver = true;

    JFrame endFrame = new JFrame();
    String displayInfo = ("Game Over! You managed to survive " + secondsSinceStart + " seconds. Consider playing again!");
    JLabel label = new javax.swing.JLabel(displayInfo);

    label.setBounds(20, 50, 600, 40);
    endFrame.add(label);
    endFrame.setSize(720, 480);
    endFrame.setLayout(null);
    // make the frame visible
    endFrame.setVisible(true);
  }
}