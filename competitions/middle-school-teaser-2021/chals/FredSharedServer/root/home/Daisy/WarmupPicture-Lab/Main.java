import javax.swing.*;
import java.awt.event.*;
import java.util.*;
import java.awt.*;
import java.io.*;

public class Main {
  public static void main(String[] args) throws InterruptedException {  
        Picture arch = new Picture("arch.jpg");
       
        // switchColors() is defined in the Picture.java file
        //arch.switchColors();
        arch.mirrorVertical();
        //TODO Challenge - Change just the flowers from red to blue - leaving the rest of the picture the same
        //arch.blueFlowers();
        arch.show();
        //Thread.sleep(10000);
        System.out.println("Test");

      }
} 
