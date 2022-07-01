import static javax.swing.JOptionPane.showMessageDialog;
import java.util.ArrayList;
import javax.swing.*;
import java.awt.*;
import javax.swing.border.*;
import javax.swing.BorderFactory;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;
import java.util.Arrays;
import java.util.Collections;

public class CoderGUI extends JFrame{
  private Codable myCoder;
  private JTextArea txtPlainText;
  private JTextArea txtCipherText;
  private JTextArea caesarShift;
  private JButton btnCode;
  private JButton btnDecode;
  private String card;
  private JButton btnRandKey;
  private JButton btnDefaultKey;
  private JTextArea subKey;
  private JTextArea atbashKey;
  private JButton btnRandKey2;
  private JButton btnDefaultKey2;
  private JFrame f;
  private JFrame fr;


  public CoderGUI(){
    this.setSize(750,550);
    this.setDefaultCloseOperation(DISPOSE_ON_CLOSE); //stops running

    // *** PLAIN TEXT ***
    txtPlainText = new JTextArea();
    txtPlainText.setPreferredSize(new Dimension(250,450));
    txtPlainText.setLineWrap(true);
    this.add(txtPlainText, BorderLayout.WEST);
    // *** PLAIN TEXT BORDER***
    TitledBorder titledBorder = BorderFactory.createTitledBorder(BorderFactory.createLineBorder(Color.black), "Plain Text");
    titledBorder.setTitleJustification(TitledBorder.CENTER);
    txtPlainText.setBorder(titledBorder);
    this.add(txtPlainText, BorderLayout.WEST);
    // *** CIPHER TEXT ***
    txtCipherText = new JTextArea();
    txtCipherText.setPreferredSize(new Dimension(250,450));
    txtCipherText.setLineWrap(true);
    this.add(txtCipherText, BorderLayout.EAST);
    // *** CIPHER TEXT BORDER***
    TitledBorder titledBorder2 = BorderFactory.createTitledBorder(BorderFactory.createLineBorder(Color.black), "Cipher Text");
    titledBorder2.setTitleJustification(TitledBorder.CENTER);
    txtCipherText.setBorder(titledBorder2);
    this.add(txtCipherText, BorderLayout.EAST);

    CardLayout c = new CardLayout();
    JPanel cardHolder = new JPanel(c);

    //*** WELCOME PANEL ***
    JPanel welcomePane = new JPanel();
    welcomePane.setLayout(new GridBagLayout());
    GridBagConstraints gc0 = new GridBagConstraints();    

    JLabel welcomeTitle = new JLabel("Welcome!\n\n");
    gc0.weightx = 0.5;    
    gc0.fill = GridBagConstraints.HORIZONTAL;    
    gc0.gridx = 0;    
    gc0.gridy = 0;    
    welcomePane.add(welcomeTitle, gc0);    

    JTextArea welcomeIntro = new JTextArea("Welcome to this encoder/decoder software! There are 3 ciphers to choose from: Caesar, Substitution, and Atbash. Click each one to learn more and enter in your text to test it out!");
    welcomeIntro.setWrapStyleWord(true);
    welcomeIntro.setLineWrap(true);
    welcomeIntro.setEditable(false);
    gc0.weightx = 0.5;    
    gc0.fill = GridBagConstraints.HORIZONTAL;    
    gc0.gridx = 0;    
    gc0.gridy = 2;    
    welcomePane.add(welcomeIntro, gc0); 

    c.show(cardHolder, "Welcome");

    //*** CAESAR PANEL ***
    JPanel caesarPane = new JPanel();
    caesarPane.setLayout(new GridBagLayout());
    GridBagConstraints gc = new GridBagConstraints();    

    JLabel caesarTitle = new JLabel("Caesar Cipher\n\n");
    gc.weightx = 0.5;    
    gc.fill = GridBagConstraints.HORIZONTAL;    
    gc.gridx = 0;    
    gc.gridy = 0;    
    caesarPane.add(caesarTitle, gc);    

    JTextArea caesarIntro = new JTextArea("The Caesar Cipher, also known as the Shift Cipher, substitutes a letter in the alphabet with another letter in the alphabet, as denoted by the shift. Enter your shift here!");
    caesarIntro.setWrapStyleWord(true);
    caesarIntro.setLineWrap(true);
    caesarIntro.setEditable(false);
    gc.weightx = 0.5;    
    gc.fill = GridBagConstraints.HORIZONTAL;    
    gc.gridx = 0;    
    gc.gridy = 2;    
    caesarPane.add(caesarIntro, gc); 

    caesarShift = new JTextArea();
    caesarShift.setPreferredSize(new Dimension(50,20));
    caesarShift.setLineWrap(true);
    TitledBorder shiftBorder = BorderFactory.createTitledBorder(BorderFactory.createLineBorder(Color.black));
    shiftBorder.setTitleJustification(TitledBorder.CENTER);
    caesarShift.setBorder(shiftBorder);
    gc.weightx = 0.5;    
    gc.fill = GridBagConstraints.HORIZONTAL;    
    gc.gridx = 0;    
    gc.gridy = 4;    
    caesarPane.add(caesarShift, gc); //END OF CAESAR PANEL

    

    //***SUB PANEL***
    JPanel subPane = new JPanel();
    subPane.setLayout(new GridBagLayout());
    GridBagConstraints gc1 = new GridBagConstraints();    

    JLabel subTitle = new JLabel("Substitution Cipher\n\n");
    gc.weightx = 0.5;    
    gc.fill = GridBagConstraints.HORIZONTAL;    
    gc.gridx = 0;    
    gc.gridy = 0;    
    subPane.add(subTitle, gc1);    

    JTextArea subIntro = new JTextArea("The Substitution Cipher replaces every letter with a different letter according to a key that contains all 26 letters of the alphabet. You can use the default key [ZYXWVUTSRQPONMLKJIHGFEDCBA], generate a random key, or enter your own!");
    subIntro.setWrapStyleWord(true);
    subIntro.setLineWrap(true);
    subIntro.setEditable(false);
    gc1.weightx = 0.5;    
    gc1.fill = GridBagConstraints.HORIZONTAL;    
    gc1.gridx = 0;    
    gc1.gridy = 2;    
    subPane.add(subIntro, gc1); 

    subKey = new JTextArea();
    subKey.setPreferredSize(new Dimension(50,20));
    subKey.setLineWrap(true);
    TitledBorder keyBorder = BorderFactory.createTitledBorder(BorderFactory.createLineBorder(Color.black));
    keyBorder.setTitleJustification(TitledBorder.CENTER);
    subKey.setBorder(keyBorder);
    gc1.weightx = 0.5;    
    gc1.fill = GridBagConstraints.HORIZONTAL;    
    gc1.gridx = 0;    
    gc1.gridy = 3;    
    subPane.add(subKey, gc1);

    
    
    btnRandKey = new JButton("Generate Random Key");
    gc1.weightx = 0.5;    
    gc1.fill = GridBagConstraints.HORIZONTAL;    
    gc1.gridx = 0;    
    gc1.gridy = 4;    
    subPane.add(btnRandKey, gc1); 
    btnDefaultKey = new JButton("Use Default Key");
    gc1.weightx = 0.5;    
    gc1.fill = GridBagConstraints.HORIZONTAL;    
    gc1.gridx = 0;    
    gc1.gridy = 5;    
    subPane.add(btnDefaultKey, gc1); 

    //***ATBASH PANEL***
    JPanel atbashPane = new JPanel();
    atbashPane.setLayout(new GridBagLayout());
    GridBagConstraints gc2 = new GridBagConstraints();    

    JLabel atbashTitle = new JLabel("Atbash Cipher\n\n");
    gc2.weightx = 0.5;    
    gc2.fill = GridBagConstraints.HORIZONTAL;    
    gc2.gridx = 0;    
    gc2.gridy = 0;    
    atbashPane.add(atbashTitle, gc2);    

    JTextArea atbashIntro = new JTextArea("The Atbash Cipher is a monoalphabetic substitution cipher originally used to encrypt the Hebrew alphabet. It is commonly known as the Mirror Cipher and reverses the key entered by the user to encrypt/decrypt the text. Enter your key below!");
    atbashIntro.setWrapStyleWord(true);
    atbashIntro.setLineWrap(true);
    atbashIntro.setEditable(false);
    gc2.weightx = 0.5;    
    gc2.fill = GridBagConstraints.HORIZONTAL;    
    gc2.gridx = 0;    
    gc2.gridy = 2;    
    atbashPane.add(atbashIntro, gc2); 

    atbashKey = new JTextArea();
    atbashKey.setPreferredSize(new Dimension(50,20));
    atbashKey.setLineWrap(true);
    TitledBorder keyBorder2 = BorderFactory.createTitledBorder(BorderFactory.createLineBorder(Color.black));
    keyBorder2.setTitleJustification(TitledBorder.CENTER);
    atbashKey.setBorder(keyBorder2);
    gc2.weightx = 0.5;    
    gc2.fill = GridBagConstraints.HORIZONTAL;    
    gc2.gridx = 0;    
    gc2.gridy = 4;    
    atbashPane.add(atbashKey, gc2); 
    
    btnRandKey2 = new JButton("Generate Random Key");
    gc2.weightx = 0.5;    
    gc2.fill = GridBagConstraints.HORIZONTAL;    
    gc2.gridx = 0;    
    gc2.gridy = 5;    
    atbashPane.add(btnRandKey2, gc2); 

    btnDefaultKey2 = new JButton("Use Default Key");
    gc2.weightx = 0.5;    
    gc2.fill = GridBagConstraints.HORIZONTAL;    
    gc2.gridx = 0;    
    gc2.gridy = 6;    
    atbashPane.add(btnDefaultKey2, gc2); 
    
    //END OF ATBASH PANEL

    cardHolder.add(welcomePane, "Welcome");
    cardHolder.add(caesarPane, "Caesar");
    cardHolder.add(subPane, "Sub");
    cardHolder.add(atbashPane, "Atbash");
    this.add(cardHolder, BorderLayout.CENTER);
     
    JPanel pnlButtonPane = new JPanel();
    pnlButtonPane.setPreferredSize(new Dimension(750,50));
    pnlButtonPane.setLayout(new BoxLayout(pnlButtonPane, BoxLayout.X_AXIS));
    JButton btnCaesar = new JButton("Caesar");
    JButton btnSub = new JButton("Substitution");
    JButton btnAtbash = new JButton("Atbash"); 

    pnlButtonPane.add(Box.createHorizontalGlue());
    pnlButtonPane.add(btnCaesar);
    pnlButtonPane.add(Box.createHorizontalGlue());
    pnlButtonPane.add(btnSub);
    pnlButtonPane.add(Box.createHorizontalGlue());
    pnlButtonPane.add(btnAtbash); 
    pnlButtonPane.add(Box.createHorizontalGlue());
    this.add(pnlButtonPane, BorderLayout.NORTH);

    JPanel pnlCodeDecodePane = new JPanel();
    pnlCodeDecodePane.setPreferredSize(new Dimension(750,50));
    pnlCodeDecodePane.setLayout(new BoxLayout(pnlCodeDecodePane, BoxLayout.X_AXIS));
    btnCode = new JButton("Encode");
    btnDecode = new JButton("Decode");
    pnlCodeDecodePane.add(Box.createHorizontalGlue());
    pnlCodeDecodePane.add(btnCode);
    pnlCodeDecodePane.add(Box.createHorizontalGlue());
    pnlCodeDecodePane.add(btnDecode);
    pnlCodeDecodePane.add(Box.createHorizontalGlue());
    this.add(pnlCodeDecodePane, BorderLayout.SOUTH);

    btnCaesar.addActionListener(new ActionListener(){
      @Override
      public void actionPerformed(ActionEvent e){
        c.show(cardHolder, "Caesar");
        card = "Caesar";
      }
    });

    btnSub.addActionListener(new ActionListener(){
      @Override
      public void actionPerformed(ActionEvent e){
        c.show(cardHolder, "Sub");
        card = "Sub";
      }
    });

    btnAtbash.addActionListener(new ActionListener(){
      @Override
      public void actionPerformed(ActionEvent e){
        c.show(cardHolder, "Atbash");
        card = "Atbash";
      }
    });

    btnCode.addActionListener(new ButtonListener());
    btnDecode.addActionListener(new ButtonListener());
    btnDefaultKey.addActionListener(new ButtonListener());
    btnRandKey.addActionListener(new ButtonListener());
    btnDefaultKey2.addActionListener(new ButtonListener());
    btnRandKey2.addActionListener(new ButtonListener());

    
    
  }
  class ButtonListener implements ActionListener {
    
     public String randomKey(){
      ArrayList<Character> upperList = new ArrayList<Character>(Arrays.asList('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'));
      Collections.shuffle(upperList);
      String newKey = "";
      for (int i=0; i<upperList.size(); i++){
        newKey += Character.toString(upperList.get(i));
      }
      return newKey;
    }

    @Override
     public void actionPerformed(ActionEvent event) {
       fr = new JFrame();
       //if (myCoder == null){
          //JOptionPane.showMessageDialog(fr, "Choose a Coder First!");
          //return;
        //}
        
        if (event.getSource() == btnCode){
          f = new JFrame();

          if (txtPlainText.getText().length() == 0){
            JOptionPane.showMessageDialog(f, "Please enter your plain text first!");
            return;
          }


          if(card.equals("Caesar")){
            
            boolean e = true;
            for (int i=0; i<caesarShift.getText().length(); i++){
              if (!(Character.isDigit(caesarShift.getText().charAt(i)))){
                JOptionPane.showMessageDialog(f, "Only enter in a number between 1 and 26!");
                e = false;
              }
            }
            if (caesarShift.getText().length() == 0){
                JOptionPane.showMessageDialog(f, "Enter in a shift!");
                e = false;
            }
            
            if (e){
              myCoder = new CaesarCipher(Integer.valueOf(caesarShift.getText())%26);
              String output = myCoder.encode(txtPlainText.getText());
              txtCipherText.setText(output);
            }

          } else if (card.equals("Sub")){
            myCoder = new SubstitutionCipher(subKey.getText());
            boolean encode = true;

            if (subKey.getText().length() == 26){
            for (int i=0; i<26; i++){
              if (!(Character.isLetter(subKey.getText().charAt(i)))){
                JOptionPane.showMessageDialog(f, "Only enter each of the 26 letters exactly once, no numbers or special characters!");
                encode = false;
              }
              for (int x=i+1; x<26; x++){
                if (subKey.getText().charAt(i) == subKey.getText().charAt(x)){
                  JOptionPane.showMessageDialog(f, "Only enter each of the 26 letters once!");
                  encode = false;
                }
              }
            }
          } else if (subKey.getText().length() < 26){
            JOptionPane.showMessageDialog(f, "You've entered less than 26 letters. Only enter each of the 26 letters, no numbers or special characters!");
            encode = false;
          } else if (subKey.getText().length() > 26){
            JOptionPane.showMessageDialog(f, "You've entered more than 26 letters. Only enter each of the 26 letters, no numbers or special characters!");
            encode = false;
          }
            if (encode){
              String output = myCoder.encode(txtPlainText.getText());
              txtCipherText.setText(output);
            }
        
          } else if (card.equals("Atbash")){
            myCoder = new AtbashCipher(atbashKey.getText());
            boolean encodeA = true;
            
            if (atbashKey.getText().length() == 26){
            for (int i=0; i<26; i++){
              if (!(Character.isLetter(atbashKey.getText().charAt(i)))){
                JOptionPane.showMessageDialog(f, "Only enter each of the 26 letters exactly once, no numbers or special characters!");
                encodeA = false;
              }
              for (int x=i+1; x<26; x++){
                if (atbashKey.getText().charAt(i) == atbashKey.getText().charAt(x)){
                  JOptionPane.showMessageDialog(f, "Only enter each of the 26 letters once!");
                  encodeA = false;
                }
              }
            }
          } else if (atbashKey.getText().length() < 26){
            JOptionPane.showMessageDialog(f, "You've entered less than 26 letters. Only enter each of the 26 letters, no numbers or special characters!");
            encodeA = false;
          } else if (atbashKey.getText().length() > 26){
              JOptionPane.showMessageDialog(f, "You've entered more than 26 letters. Only enter each of the 26 letters, no numbers or special characters!");
              encodeA = false;
          }
          if (encodeA){
              String output = myCoder.encode(txtPlainText.getText());
              txtCipherText.setText(output);
          }
        }

        } else if (event.getSource() == btnDecode){

          if (txtCipherText.getText().length() == 0){
            JOptionPane.showMessageDialog(f, "Please enter your cipher text first!");
            return;
          }

          if(card.equals("Caesar")){
            myCoder = new CaesarCipher(Integer.valueOf(caesarShift.getText())%26);
            String output = myCoder.decode(txtCipherText.getText());
            txtPlainText.setText(output);
          } else if (card.equals("Sub")){
            boolean decode = true;
            myCoder = new SubstitutionCipher(subKey.getText());
              

            if (subKey.getText().length() == 26){
            for (int i=0; i<26; i++){
              if (!(Character.isLetter(subKey.getText().charAt(i)))){
                JOptionPane.showMessageDialog(f, "Only enter each of the 26 letters exactly once, no numbers or special characters!");
                decode = false;
              }
              for (int x=i+1; x<26; x++){
                if (subKey.getText().charAt(i) == subKey.getText().charAt(x)){
                  JOptionPane.showMessageDialog(f, "Only enter each of the 26 letters once!");
                  decode = false;
                }
              }
            }
          } else if (subKey.getText().length() < 26){
            JOptionPane.showMessageDialog(f, "You've entered less than 26 letters. Only enter each of the 26 letters, no numbers or special characters!");
            decode = false;
          } else if (subKey.getText().length() > 26){
              JOptionPane.showMessageDialog(f, "You've entered more than 26 letters. Only enter each of the 26 letters, no numbers or special characters!");
              decode = false;
          }
  
          if (decode){
            String output = myCoder.decode(txtCipherText.getText());
            txtPlainText.setText(output);  
          }
           

          } else if (card.equals("Atbash")){
            boolean decodeA = true;
            myCoder = new AtbashCipher(atbashKey.getText());
            
            if (atbashKey.getText().length() == 26){
            for (int i=0; i<26; i++){
              if (!(Character.isLetter(atbashKey.getText().charAt(i)))){
                JOptionPane.showMessageDialog(f, "Only enter each of the 26 letters exactly once, no numbers or special characters!");
                decodeA = false;
              }
              for (int x=i+1; x<26; x++){
                if (atbashKey.getText().charAt(i) == atbashKey.getText().charAt(x)){
                  JOptionPane.showMessageDialog(f, "Only enter each of the 26 letters once!");
                  decodeA = false;;
                }
              }
            }
          } else if (atbashKey.getText().length() < 26){
            JOptionPane.showMessageDialog(f, "You've entered less than 26 letters. Only enter each of the 26 letters, no numbers or special characters!");
            decodeA = false;;
          } else if (atbashKey.getText().length() > 26){
              JOptionPane.showMessageDialog(f, "You've entered more than 26 letters. Only enter each of the 26 letters, no numbers or special characters!");
              decodeA = false;;
          }  
          if (decodeA){
            String output = myCoder.decode(txtCipherText.getText());
            txtPlainText.setText(output);
          }
          
          }
        }
        
        if (event.getSource() == btnDefaultKey){
          subKey.setText("ZYXWVUTSRQPONMLKJIHGFEDCBA");
        } else if (event.getSource() == btnRandKey){
          subKey.setText(randomKey());
        } else if (event.getSource() == btnDefaultKey2){
          atbashKey.setText("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
        } if (event.getSource() == btnRandKey2){
          atbashKey.setText(randomKey());
        }
      }
  }

}