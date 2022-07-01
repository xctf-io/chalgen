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

public class TextBox extends GameObject{
	
	private float width = 48, height = 96;
	private String text = "";
	
	
	public TextBox(float x, float y,ObjectId id) {
		super(x, y, id);
	}
	public void tick(LinkedList<GameObject> object) {

	}
	
	public void render(Graphics g) {
		Font stringFont = new Font("SansSerif",Font.PLAIN,25);
		g.setFont(stringFont);
		g.setColor(Color.white);
		g.drawString(text,(int)x,(int)y);
		
	}
	
	public void setText(String str) {
		text=str;
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
