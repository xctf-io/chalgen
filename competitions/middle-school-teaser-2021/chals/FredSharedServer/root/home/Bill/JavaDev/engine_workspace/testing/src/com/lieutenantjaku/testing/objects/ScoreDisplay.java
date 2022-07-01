package com.lieutenantjaku.testing.objects;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.util.LinkedList;

import com.lieutenantjaku.testing.framework.GameObject;
import com.lieutenantjaku.testing.framework.KeyInput;
import com.lieutenantjaku.testing.framework.ObjectId;
import com.lieutenantjaku.testing.window.Handler;

public class ScoreDisplay extends GameObject{
	
	private float width = 48, height = 96;
	private Handler handler;
	private Player player;
	private String numS = "";
	private int num = 0;
	
	public ScoreDisplay(float x, float y, Handler handler,ObjectId id,Player play) {
		super(x, y, id);
		this.handler = handler;
		player= play;
	}
	KeyInput input = (new KeyInput(handler));
	public void tick(LinkedList<GameObject> object) {
		y = player.getY()-375;
		x = player.getX()-375;
		num = (int)player.getScore();
		
	}
	
	public void render(Graphics g) {
		Font stringFont = new Font("SansSerif",Font.PLAIN,25);
		numS=""+num;
		g.setFont(stringFont);
		g.setColor(Color.blue);
		g.drawString("Score: "+numS,(int)x,(int)y);
		for(int i=0;i<player.getHealth();i++){
			g.setColor(Color.green);
			if (player.getHealth()<=50){
				g.setColor(Color.yellow);
			}
			if (player.getHealth()<=25){
				g.setColor(Color.red);
			}
			g.drawString("|",((int)x+(i)),((int)y+25));
		}
		
		/*Graphics2D g2d = (Graphics2D) g;
		g.setColor(Color.red);
		g2d.draw(getBounds());
		g2d.draw(getBoundsRight());
		g2d.draw(getBoundsLeft());
		g2d.draw(getBoundsTop());*/
	}

	public Rectangle getBounds() {
		return new Rectangle((int)x+(int)width/2-(((int)width/2)/2),(int)y+(int)height/2,(int)width/2,(int)height/2);
	}
	public Rectangle getBoundsTop() {
		return new Rectangle((int)x+(int)width/2-(((int)width/2)/2),(int)y,(int)width/2,(int)height/2);
	}
	public Rectangle getBoundsRight() {
		return new Rectangle((int)x+(int)width-5,(int)y+5,(int)5,(int)height-10);
	}
	public Rectangle getBoundsLeft() {
		return new Rectangle((int)x,(int)y+5,(int)5,(int)height-10);
	}

}
