package code;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFClientAnchor;
import org.apache.poi.xssf.usermodel.XSSFDrawing;
import org.apache.poi.xssf.usermodel.XSSFPicture;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.MatOfByte;
import org.opencv.core.MatOfDouble;
import org.opencv.core.MatOfPoint;
import org.opencv.core.Point;
import org.opencv.core.Rect;
import org.opencv.core.Scalar;
import org.opencv.core.Size;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.videoio.VideoCapture;
import org.opencv.videoio.Videoio;
import org.opencv.imgproc.Moments;

import extra.Utils;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.Slider;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.text.Text;

public class AppController
{
	@FXML
	private Text r;
	@FXML
	private Text g;
	@FXML
	private Text b;
	// the FXML button
	@FXML
	private Button button;
	@FXML
	private Button save;
	@FXML
	private Slider lightSlider;
	@FXML
	private ImageView currentFrame;
	@FXML
	private CheckBox masked;
	@FXML
	private Text rock;
	@FXML
	private Text area;
	@FXML
	private Text crystal;
	@FXML
	private ImageView check;
	@FXML
	private ImageView check1;
	@FXML
	private ImageView savedImage;
	
	public static String[] ints = {"", "", "", ""};
	// a timer for acquiring the video stream
	private ScheduledExecutorService timer;
	// the OpenCV object that realizes the video capture
	public static VideoCapture capture;
	// a flag to change the button behavior
	private boolean cameraActive;
	
	private static Point clickedPoint = new Point(0, 0);
	private Mat currentDisplay = new Mat();
	private static double pixelToInch;
	private int crystalNum = 35;
	
	private static Sheet sheet = App.wb.createSheet("Data");
	private static String[] columns = {"Time Taken", "Rock Type", "Red", "Blue", "Green", "Area", "Crystals", "Images"};
	private int rowNum = 1;
	private CellStyle rowStyle = App.wb.createCellStyle();
	/**
	 * Initialize method, automatically called by @{link FXMLLoader}
	 */
	public void initialize()
	{
		Font headerFont = App.wb.createFont();
        headerFont.setBold(true);
        headerFont.setFontHeightInPoints((short) 30);
        headerFont.setColor(IndexedColors.RED.getIndex());
        // Create a CellStyle with the font
        CellStyle headerCellStyle = App.wb.createCellStyle();
        headerCellStyle.setFont(headerFont);
        headerCellStyle.setAlignment(HorizontalAlignment.CENTER);
        Row headerRow = sheet.createRow(0);

        // Create cells
        for (int i = 0; i < columns.length; i++) {
            Cell cell = headerRow.createCell(i);
            cell.setCellValue(columns[i]);
            cell.setCellStyle(headerCellStyle);
        }
        Font rowFont = App.wb.createFont();
        rowFont.setFontHeightInPoints((short) 24);
        rowStyle.setFont(rowFont);
        rowStyle.setVerticalAlignment(VerticalAlignment.CENTER);
        
		this.capture = new VideoCapture();
		this.cameraActive = false;
		lightSlider.setDisable(true);
		updateImageView(savedImage, Utils.mat2Image(Imgcodecs.imread("resources/init.png")));
		//add Listeners to update rgb values of light
		currentFrame.setOnMouseClicked(e -> {
			System.out.println("Mouse Click at: " + e.getX() + ", " + e.getY());
			clickedPoint.x = e.getX();
			clickedPoint.y = e.getY();
		});
		lightSlider.valueProperty().addListener(new ChangeListener<Number>() {
            public void changed(ObservableValue<? extends Number> ov,
                Number old_val, Number new_val) {
            		String val = "" + new_val.intValue();
            		val = "c" + "0".repeat(3-val.length()) + val;
            		App.light = val;
            }
        });
	}
	
	/**
	 * The action triggered by pushing the button on the GUI
	 */
	@FXML
	protected void startCamera()
	{
		// set a fixed width for the frame
		this.currentFrame.setFitWidth(600);
		// preserve image ratio
		this.currentFrame.setPreserveRatio(true);
		
		if (!this.cameraActive)
		{
			// start the video capture
			this.capture.open(0);
			//change this to max resolution of camera
			//this.capture.set(Videoio.CAP_PROP_FRAME_WIDTH, 1280);
			//this.capture.set(Videoio.CAP_PROP_FRAME_HEIGHT, 720);
			
			// is the video stream available?
			if (this.capture.isOpened())
			{
				this.cameraActive = true;
				double val = findRock(true)[0];
				pixelToInch = App.reference / val;
				// grab a frame every 33 ms (30 frames/sec)
				Runnable frameGrabber = new Runnable() {
					
					@Override
					public void run()
					{
						// effectively grab and process a single frame
						Mat frame = grabFrame();
						// convert and show the frame
						if (!masked.isSelected()) {
							currentDisplay = frame;
							Image imageToShow = Utils.mat2Image(currentDisplay);
							updateImageView(currentFrame, imageToShow);
							double[] vals = getBGR(currentDisplay);
							for(int i = 0; i < 3; i++) {
								ints[i] = ((int) vals[i]) + "";
							}
							b.setText("B = " + ints[0]);
							g.setText("G = " + ints[1]);
							r.setText("R = " + ints[2]);
							area.setText("Area:\nN/a");
							crystal.setText("Crystals:\nN/a");
							int total = (int) (vals[0] + vals[1] + vals[2]);
							if(total < 275) {
								rock.setText("Rock Type:\nMafic");
							}
							else if (total < 325) {
								rock.setText("Rock Type:\nIntermediate");
							}
							else {
								rock.setText("Rock Type:\nFelsic");
							}
						}
						else {
							double[] vals = findRock(false);
							for(int i = 0; i < 3; i++) {
								ints[i] = ((int) vals[i]) + "";
							}
							b.setText("B = " + ints[0]);
							g.setText("G = " + ints[1]);
							r.setText("R = " + ints[2]);
							ints[3] = (double)(Math.round(vals[3] * 1000)) / 1000 + "";
							area.setText("Area:\n" + ints[3] + " in\u00b2");
							int total = (int) (vals[0] + vals[1] + vals[2]);
							if(findCrystals(currentDisplay)) {
								if(total < 275) {
									rock.setText("Rock Type:\nMafic");
								}
								else if (total < 325) {
									rock.setText("Rock Type:\nIntermediate");
								}
								else {
									rock.setText("Rock Type:\nFelsic");
								}
								crystal.setText("Crystals:\nYes");
							} else {
								crystal.setText("Crystals:\nNo");
								rock.setText("Rock Type:\nFelsic"); //all glassy rocks must be felsic
							}
						}
						if(App.drillOn) {
							updateImageView(check, Utils.mat2Image(Imgcodecs.imread("resources/check.png")));				
						} else {
							updateImageView(check, Utils.mat2Image(Imgcodecs.imread("resources/cross.png")));
						}
						if(App.lightOn) {
							lightSlider.setDisable(false);
							updateImageView(check1, Utils.mat2Image(Imgcodecs.imread("resources/check.png")));				
						} else {
							lightSlider.setDisable(true);
							updateImageView(check1, Utils.mat2Image(Imgcodecs.imread("resources/cross.png")));
						}
					}
				};
				
				this.timer = Executors.newSingleThreadScheduledExecutor();
				this.timer.scheduleAtFixedRate(frameGrabber, 0, 33, TimeUnit.MILLISECONDS);
				
				// update the button content
				this.button.setText("Stop Camera");
			}
			else
			{
				// log the error
				System.err.println("Impossible to open the camera connection...");
			}
		}
		else
		{
			// the camera is not active at this point
			this.cameraActive = false;
			// update again the button content
			this.button.setText("Start Camera");
			
			// stop the timer
			this.stopAcquisition();
		}
	}
	
	
	/**
	 * Get a frame from the opened video stream (if any)
	 * 
	 * @return the {@link Image} to show
	 */
	private Mat grabFrame()
	{
		Mat frame = new Mat();
		// check if the capture is open
		if (this.capture.isOpened())
		{
			try
			{
				// read the current frame
				this.capture.read(frame);
			}
			catch (Exception e)
			{
				// log the error
				System.err.println("Exception during the frame elaboration: " + e);
			}
		}
		return frame;
	}
	
	/**
	 * Stop the acquisition from the camera and release all the resources
	 */
	private void stopAcquisition()
	{
		if (this.timer != null && !this.timer.isShutdown())
		{
			try
			{
				// stop the timer
				this.timer.shutdown();
				this.timer.awaitTermination(33, TimeUnit.MILLISECONDS);
			}
			catch (InterruptedException e)
			{
				// log any exception
				System.err.println("Exception in stopping the frame capture, trying to release the camera now... " + e);
			}
		}
		
		if (this.capture.isOpened())
		{
			// release the camera
			this.capture.release();
		}
	}
	private boolean findCrystals(Mat frame) {
		Mat edges = doCanny(frame);
		List<MatOfPoint> contours = new ArrayList<>();
		Imgproc.findContours(edges, contours,  new Mat(), 
		Imgproc.RETR_LIST, Imgproc.CHAIN_APPROX_SIMPLE);
		return contours.size() > crystalNum;
	}
	private Mat doCanny(Mat frame)
	{
		Mat grayImage = new Mat();
		Mat detectedEdges = new Mat();
		Imgproc.cvtColor(frame, grayImage, Imgproc.COLOR_BGR2GRAY);
		Imgproc.blur(grayImage, detectedEdges, new Size(3, 3));
		Imgproc.Canny(detectedEdges, detectedEdges, 20, 60);	
		Mat dst = new Mat();
		frame.copyTo(dst, detectedEdges);
		Imgproc.cvtColor(dst, dst, Imgproc.COLOR_BGR2GRAY);
		Imgproc.dilate(dst, dst, new Mat());
		Imgproc.erode(dst, dst, new Mat());
		return dst;
	}
	private double[] findRock(boolean start) {
		double[] ret = new double[4];
		Mat copy = grabFrame();
		Mat edges =  doCanny(copy); //canny edge detection
		List<MatOfPoint> contours = new ArrayList<>();
		//use edges to find contours
		Imgproc.findContours(edges, contours,  new Mat(), Imgproc.RETR_EXTERNAL, Imgproc.CHAIN_APPROX_SIMPLE); 
		Scalar color = new Scalar(255, 255, 255); //white
		//index of largest area nearest to cursor
		int index = findLargestArea(contours,start); 
		if(start) {
			//return reference area in pixels
			ret[0]= Imgproc.contourArea(contours.get(index)); 
			return ret;
		}
		Rect crop = Imgproc.boundingRect(contours.get(index)); 
		//draw contours at index
		Imgproc.drawContours(copy, contours, index, color, 2); 
		Mat mask = Mat.zeros(copy.size(), 0);
		Imgproc.drawContours(mask, contours, index, color, -1);
		Mat temp = grabFrame();
		Mat object = new Mat();
		Core.bitwise_and(temp, temp, object, mask);
		Image imageToShow = Utils.mat2Image(object);
		//update currently showing image
		currentDisplay = new Mat(object, crop);
		updateImageView(currentFrame, imageToShow); 	
		//get RGB values
		MatOfDouble mean = new MatOfDouble();
		MatOfDouble dev = new MatOfDouble();
		Core.meanStdDev(temp, mean, dev, mask);
		double[] arr = mean.toArray();
		for(int x = 0; x < arr.length; x++) {
			ret[x] = arr[x];
		}
		//multiply area by ratio found using the reference
		ret[3] = Imgproc.contourArea(contours.get(index)) * pixelToInch; 
		return ret;
	}
	private void updateImageView(ImageView view, Image image)
	{
		Utils.onFXThread(view.imageProperty(), image);
	}
	
	public static int findLargestArea(List<MatOfPoint> contours, boolean notClick) {
		Mat max = contours.get(0);
		int index = 0;
		for(int i = 0; i < contours.size(); i++) {
			Moments moments = Imgproc.moments(contours.get(i));
			double x = moments.get_m10() / moments.get_m00();
			double y = moments.get_m01() / moments.get_m00();
			if(Imgproc.contourArea(max) < Imgproc.contourArea(contours.get(i))) {
				if(notClick || (y > clickedPoint.y - 50 && y < clickedPoint.y + 50 && x > clickedPoint.x - 50 && x < clickedPoint.x + 50)) {
					max = contours.get(i);
					index = i;
				}
			}
		}
		return index;
	}
	
	/**
	 * On application close, stop the acquisition from the camera
	 */
	protected void setClosed()
	{
		this.stopAcquisition();
	}
	
	public static boolean on() {
		return capture.isOpened();
	}
	
	public static double[] getBGR(Mat image) {
		MatOfDouble mean = new MatOfDouble();
		MatOfDouble dev = new MatOfDouble();
		Core.meanStdDev(image, mean, dev);
		return mean.toArray();
	}

	//save the data
	@FXML
	protected void saved()
	{
		Mat img = currentDisplay.clone();
		updateImageView(savedImage, Utils.mat2Image(img));
		//convert mat to bytes
		MatOfByte matOfByte = new MatOfByte(); 
	    Imgcodecs.imencode(".jpg", img, matOfByte);
	    byte[] byteArray = matOfByte.toArray();
	    //create spreadsheet
		Row row = sheet.createRow(rowNum);
		SimpleDateFormat formatter = new SimpleDateFormat("HH:mm:ss");
		Date date = new Date(System.currentTimeMillis());
		int height = 3000;
		row.setHeight((short) height);
		row.setRowStyle(rowStyle);
		row.createCell(0).setCellValue(formatter.format(date)); 
		row.createCell(1).setCellValue(rock.getText().substring(rock.getText().indexOf("\n") + 1));
		row.createCell(2).setCellValue(r.getText().substring(4));
		row.createCell(3).setCellValue(g.getText().substring(4));
		row.createCell(4).setCellValue(b.getText().substring(4));
		row.createCell(5).setCellValue(area.getText().substring(area.getText().indexOf("\n") + 1));
		row.createCell(6).setCellValue(crystal.getText().substring(area.getText().indexOf("\n") + 5));
		int picture_id = App.wb.addPicture(byteArray, Workbook.PICTURE_TYPE_JPEG);
		XSSFDrawing drawing = (XSSFDrawing) sheet.createDrawingPatriarch();
        XSSFClientAnchor my_anchor = new XSSFClientAnchor();
        my_anchor.setCol1(columns.length - 1); 
        my_anchor.setRow1(rowNum);
        my_anchor.setCol2(columns.length); 
        my_anchor.setRow2(rowNum + 1);
        XSSFPicture my_picture = drawing.createPicture(my_anchor, picture_id);
		for (int i = 0; i < columns.length - 1; i++) {
            sheet.autoSizeColumn(i);
        }
		sheet.setColumnWidth(columns.length - 1, (int)(height * 3.5));
		rowNum++;
	}
}
