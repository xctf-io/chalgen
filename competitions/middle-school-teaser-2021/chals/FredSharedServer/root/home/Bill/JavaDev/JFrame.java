//HIDE
//OUT frame.png

/**
   Replacement for javax.swing.JFrame in student programs for
   saving the output to a file. Can be put in codecheck if
   the student program has import javax.swing.*.
*/

import java.awt.image.BufferedImage;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.io.IOException;
import java.io.File;
import java.util.ArrayList;
import javax.imageio.ImageIO;
import javax.swing.JComponent;
import javax.swing.SwingUtilities;

public class JFrame
{
   private Dimension size = new Dimension(0, 0);
   private ArrayList<Component> components = new ArrayList<Component>();
   public static final int EXIT_ON_CLOSE = 0;

   public void setSize(int width, int height)
   {
      size = new Dimension(width, height);
   }

   public void setDefaultCloseOperation(int op) {}
   public void setTitle(String s) {}

   public void add(Component c) { components.add(c); }

   public void setVisible(boolean b)
   {
      String fileName = "frame.png";
      Rectangle rect = new java.awt.Rectangle(0, 0, size.width, size.height);
      BufferedImage image = new BufferedImage(rect.width, rect.height, BufferedImage.TYPE_INT_RGB);
      Graphics2D g = (Graphics2D) image.getGraphics();
      g.setColor(java.awt.Color.WHITE);
      g.fill(rect);
      g.setColor(java.awt.Color.BLACK);

      try
      {
         // That's because we can't call the protected paintComponent
         // method. SwingUtilities can because it's in the same package.
         // The parent doesn't matter--look through the source of
         // SwingUtilities.paintComponent and
         // SwingUtilities.getCellRendererPane
         SwingUtilities.paintComponent(g,
            components.get(0), new JComponent() {}, rect);

         String extension = fileName.substring(fileName.lastIndexOf('.') + 1);
         ImageIO.write(image, extension, new File(fileName));
      }
      catch(Exception e)
      {
         System.err.println("Was unable to save the image to " + fileName);
         e.printStackTrace();
      }
      g.dispose();
   }
}
