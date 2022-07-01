import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import javax.swing.*;
public class MouseComponent extends JComponent implements MouseListener {
    boolean isClicked = false;
    @Override
    public void mouseClicked(MouseEvent arg0) {
        isClicked = true;
        System.out.println("Clicked");
    }
    @Override
    public void mouseExited(MouseEvent arg0) {
      // TODO
    }
    public void mouseReleased(MouseEvent e) {
       // TODO
    }

    public void mouseEntered(MouseEvent e) {
       // TODO
    }
    public void mousePressed(MouseEvent e) {
       // TODO
    }


    public boolean IsMouseClicked() {
      boolean r = isClicked;
      isClicked = false; // So that we know what the click has been gotten by JFrame.
      return r;
    }
    

}