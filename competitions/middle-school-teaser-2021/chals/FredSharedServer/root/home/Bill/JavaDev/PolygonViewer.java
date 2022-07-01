import java.awt.geom.Point2D;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.*;

public class PolygonViewer
{
   public static void main(String[] args)
   {
      JFrame frame = new JFrame();

      final int FRAME_WIDTH = 300;
      final int FRAME_HEIGHT = 400;

      frame.setSize(FRAME_WIDTH, FRAME_HEIGHT);
      frame.setTitle("PolygonViewer");
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

      JComponent component = new JComponent()
      {
         public void paintComponent(Graphics graph)
         {
            Graphics2D g2 = (Graphics2D) graph;

            Polygon square = new Polygon();
            square.add(new Point2D.Double(100, 100));
            square.add(new Point2D.Double(100, 150));
            square.add(new Point2D.Double(150, 150));
            square.add(new Point2D.Double(150, 100));

            square.draw(g2);

            Polygon pentagon = new Polygon();
            double centerX = 200;
            double centerY = 200;
            double radius = 50;
            for (int i = 0; i < 5; i++)
            {
                double angle = 2 * Math.PI * i / 5;
                pentagon.add(new Point2D.Double(
                        centerX + radius * Math.cos(angle),
                        centerY + radius * Math.sin(angle)));
            }

            pentagon.draw(g2);
         }
      };

      frame.add(component);
      frame.setVisible(true);
   }
}
