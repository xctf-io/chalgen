wpackage com.lieutenantjaku.testing.window;

import java.awt.Canvas;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;
import java.util.Random;

import com.lieutenantjaku.testing.framework.KeyInput;
import com.lieutenantjaku.testing.framework.ObjectId;
import com.lieutenantjaku.testing.objects.Block;
import com.lieutenantjaku.testing.objects.BlueBlock;
import com.lieutenantjaku.testing.objects.Coin;
import com.lieutenantjaku.testing.objects.Damage;
import com.lieutenantjaku.testing.objects.Elevator;
import com.lieutenantjaku.testing.objects.Enemy;
import com.lieutenantjaku.testing.objects.Exit;
import com.lieutenantjaku.testing.objects.ExitGate;
import com.lieutenantjaku.testing.objects.GreenBlock;
import com.lieutenantjaku.testing.objects.Person1;
import com.lieutenantjaku.testing.objects.Player;
import com.lieutenantjaku.testing.objects.RedBlock;
import com.lieutenantjaku.testing.objects.ScoreDisplay;
import com.lieutenantjaku.testing.objects.YellowBlock;

public class Game extends Canvas implements Runnable {
	
	private static final long serialVersionUID = 9083175080527061150L;

	private boolean running = false;
	private Thread thread;
	
	
	public static int WIDTH, HEIGHT;
	
	private BufferedImage level = null;
	
	Handler handler;
	Camera cam;
	
	Random rand= new Random();
	KeyInput kinput = new KeyInput(handler);
	private void init() {
		WIDTH = getWidth();
		HEIGHT = getHeight();
		BufferedImageLoader loader = new BufferedImageLoader();
		level = loader.loadImage("/level.png"); //loading the level into variable
		handler = new Handler();
		cam = new Camera (0,0);
		//handler.addObject(new Player (100,100, handler, ObjectId.Player));
		//handler.createLevel();
		LoadImageLevel(level);
		KeyInput kinput = new KeyInput(handler);
		this.addKeyListener(kinput);
	}
	
	public synchronized void start() {
		if(running)
			return; 
			//fail-safe so the thread can't be started twice at the same time
		
		running = true;
		thread = new Thread(this);
		thread.start();	
	}
	
	public void run() {
		
		init();
		this.requestFocus();
		long lastTime = System.nanoTime();
		double amountOfTicks = 60.0;
		double ns = 1000000000 / amountOfTicks;
		double delta = 0;
		long timer = System.currentTimeMillis();
		int updates = 0;
		int frames = 0;
		while(running){
			long now = System.nanoTime();
			delta += (now - lastTime) / ns;
			lastTime = now;
			while(delta >= 1){
				tick();
				updates++;
				delta--;
			}
			render();
			frames++;
					
			if(System.currentTimeMillis() - timer > 1000){
				timer += 1000;
				//System.out.println("FPS: " + frames + " TICKS: " + updates);
				frames = 0;
				updates = 0;
			}
		}
		
	}
	
	private void tick() {
		handler.tick();
		for(int i =0; i< handler.object.size(); i++) {
			if(handler.object.get(i).getId() == ObjectId.Player) {
				cam.tick(handler.object.get(i));
			}
		}
	}
	
	private void render() {
		
		BufferStrategy bs = this.getBufferStrategy();
		if (bs == null){
			this.createBufferStrategy(3);
			return;
		}
		
		Graphics g = bs.getDrawGraphics();
		Graphics2D g2d = (Graphics2D) g;
		/////////////
		//draw here//
		g.setColor(Color.BLACK);
		g.fillRect(0, 0, getWidth(), getHeight());
		g2d.translate(cam.getX(), cam.getY()); //cam start
		handler.render(g);
		g2d.translate(-cam.getX(), -cam.getY()); //cam end
		/////////////
		
		g.dispose();
		bs.show();
	}
	
	private void LoadImageLevel(BufferedImage image) {
		int w = image.getWidth();
		int h = image.getHeight();
		
		System.out.println("width, height: "+w+", "+h);
		
		for(int xx=0; xx<h; xx++) {
			for(int yy=0; yy<w; yy++) {
				int pixel = image.getRGB(xx, yy);
				int red = (pixel >> 16) & 0xff;
				int green = (pixel >> 8) & 0xff;
				int blue = (pixel) & 0xff;
				
				if(red==255 && blue==255 && green==255) {
					handler.addObject(new Block(xx*32,yy*32,ObjectId.Block));
				}
				if(red==0 && blue==1 && green==255) {
					handler.addObject(new GreenBlock(xx*32,yy*32,ObjectId.GreenBlock));
				}
				if(red==253 && blue==33 && green==238) {
					handler.addObject(new YellowBlock(xx*32,yy*32,ObjectId.YellowBlock));
				}
				if(red==0 && blue==255 && green==255) {
					handler.addObject(new BlueBlock(xx*32,yy*32,ObjectId.BlueBlock));
				}
				if(red==254 && blue==0 && green==0) {
					handler.addObject(new RedBlock(xx*32,yy*32,ObjectId.RedBlock));
				}
				if(red==0 && blue==255 && green==0) {
					Player player=new Player(xx*32,yy*32,handler,ObjectId.Player,kinput);
					handler.addObject(player);
					handler.addObject(new ScoreDisplay((float)25,(float)25,handler,ObjectId.ScoreDisplay,player));
				}
				if(red==0 && blue==0 && green==255) {
					handler.addObject(new Elevator(xx*32,yy*32,ObjectId.Elevator));
				}
				if(red==255 && blue==0 && green==216) {
					handler.addObject(new Coin(xx*32,yy*32,ObjectId.Coin));
				}
				if(red==255 && blue==0 && green==0) {
					handler.addObject(new Damage(xx*32,yy*32,ObjectId.Damage));
				}
				if(red==255 && blue==0 && green==106) {
					handler.addObject(new Enemy(xx*32,yy*32,handler,ObjectId.Enemy,kinput,1,2));
				}
				if(red==255 && blue==220 && green==0) {
					handler.addObject(new ExitGate(xx*32,yy*32,ObjectId.ExitGate));
				}
				if(red==182 && blue==0 && green==255) {
					handler.addObject(new Exit(xx*32,yy*32,ObjectId.Exit));
				}
				if(red==87 && blue==127 && green==0) {
					String[] textP1={"...","Hi","I am a robocall", "please Ignore me"};
					handler.addObject(new Person1(xx*32,yy*32,ObjectId.Person1,textP1));
				}
			}
		}
	}
	
	public static void main(String args[]) {
		new window(800, 600, "Platformer", new Game());
}
	
}
