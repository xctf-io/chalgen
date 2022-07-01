import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;


public class CountDownClockGUI extends JFrame implements ActionListener{
	private JMenu myMenu;
	private JMenuBar menuBar;
	private JMenuItem setEndItem;
	private JMenuItem changeTxtColItm;
	private JMenuItem changeBkgdColItm;
	private JMenuItem setFontSizeItm;
	
	private CountDownClock myClock;
	private Timer myTimer;
	private JTextArea myText;
	
	
	public CountDownClockGUI(){
		super("PHS Graduation 2008 Countdown!");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setSize(575,625);
		myTimer = new Timer(500, this);
		myTimer.start();
		myText = new JTextArea();
		myText.setMargin(new Insets(40,40,40,40));
		myText.setEditable(false);
		myText.setFont(new Font("Times New Roman", Font.CENTER_BASELINE,100 ));

	//	Box aBox = new Box(1);
	//	aBox.add(myText,BorderLayout.CENTER);
		this.add(myText, BorderLayout.CENTER);
	//	this.add(aBox);
		
		myClock = new CountDownClock();
		menuBar = new JMenuBar();
		myMenu = new JMenu("Options");
		menuBar.add(myMenu);
		
		setEndItem = new JMenuItem("Set End Time");
		myMenu.add(setEndItem);
		setEndItem.addActionListener(this);
		
		changeTxtColItm = new JMenuItem("Change Text Color");
		myMenu.add(changeTxtColItm);
		changeTxtColItm.addActionListener(this);

		changeBkgdColItm = new JMenuItem("Change Background Color");
		myMenu.add(changeBkgdColItm);
		changeBkgdColItm.addActionListener(this);
		
		setFontSizeItm = new JMenuItem("Change Font");
		myMenu.add(setFontSizeItm);
		setFontSizeItm.addActionListener(this);
		
		this.setJMenuBar(menuBar);
	}
	public void actionPerformed(ActionEvent ev){
		Object source = ev.getSource();
		if(source == setEndItem){
			String year = JOptionPane.showInputDialog("Enter year (4 digits): ");
			String month = JOptionPane.showInputDialog("Enter month (1-12): ");
			String day = JOptionPane.showInputDialog("Enter day: ");
			String hour = JOptionPane.showInputDialog("Enter hour (24 hour): ");
			String minute = JOptionPane.showInputDialog("Enter minute: ");
			myClock.setEndTime(year,month,day,hour,minute);
		}else if(source == changeTxtColItm){
			Color col = JColorChooser.showDialog(this,"Text Color",myText.getForeground());
			myText.setForeground(col);  
		}else if(source == changeBkgdColItm){
			Color col = JColorChooser.showDialog(this,"Background Color",myText.getBackground());
			myText.setBackground(col);
		}else if(source == setFontSizeItm){
			FontChooser2 fc = new FontChooser2(this);
			fc.setVisible(true);
			//fc.setFont(myText.getFont());
			if(fc.getSelectedFont()!=null)
				myText.setFont(fc.getSelectedFont());
		}else if(source == myTimer){
			String time = myClock.getRemaining();
			time = time.replace("\n"," ");
			myText.setText(time);
		}
	}
	
	
	public static void main(String[] args) {
		CountDownClockGUI cdc = new CountDownClockGUI();
		cdc.setVisible(true);

	}

}
