package code;

import jssc.SerialPort;
import jssc.SerialPortException;

public class Arduino {

	public static void main(String[] args) throws SerialPortException {
		SerialPort serialPort = new SerialPort("COM3"); //Replace with name of your serial port
		serialPort.openPort();//Open serial port
        serialPort.setParams(9600, 8, 1, 0);//Set params.
	    try {
	        String s = "     ";
	        while(!s.contains("Ready")) {
		        s = new String(serialPort.readBytes(10));
	        }
	        System.out.println("Connected to Arduino!");
	        while(App.arduinoOn) {
	        	if(!App.lastColor.equals(App.light)) {
	    	        serialPort.writeBytes(App.light.getBytes());
	        		App.lastColor = App.light;
	        	}
		        s = new String(serialPort.readBytes(10));
		        s = s.substring(0, 3);
		        if(s.contains("b1")) {
		        	App.drillOn = false;
		        } else if(s.contains("b0")) {
		        	App.drillOn = true;
		        }  else if(s.contains("p0")) {
		        	App.lightOn = false;
		        }   else if(s.contains("p1")) {
		        	App.lightOn = true;
		        } else {
		        	System.out.print("");
		        }
	        }
	    }
	    catch (SerialPortException ex) {
	        System.out.println(ex);
	    }

	}

}
