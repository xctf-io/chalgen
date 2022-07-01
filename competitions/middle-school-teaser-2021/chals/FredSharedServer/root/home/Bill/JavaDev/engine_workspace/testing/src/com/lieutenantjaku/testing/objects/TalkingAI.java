package com.lieutenantjaku.testing.objects;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.util.LinkedList;

import com.lieutenantjaku.testing.framework.GameObject;
import com.lieutenantjaku.testing.framework.ObjectId;

public class TalkingAI extends GameObject{
	private String name;
	private String[] text;
	private float width = 48, height = 96;
	private int speechIndex=0;
	private TextBox bubble=new TextBox(x-32,y-32,ObjectId.TextBox);
	private TextBox nameBox=new TextBox(x-32,y,ObjectId.TextBox);
	
	public TalkingAI(float x, float y, ObjectId id,String n,String[] t) {
		super(x, y, id);
		name=n;
		text=new String[t.length];
		for (int i =0;i<text.length;i++){
			text[i]=t[i];
		}
		nameBox.setText(name);
	}

	
	public void tick(LinkedList<GameObject> object) {
		
	}
	
	public void speech(){
		if(speechIndex>0) {
			bubble.setText(text[speechIndex-1]);
		}
		speechIndex++;
		if(text.length<speechIndex) {
			speechIndex=0;
		}
	}
	
	public void render(Graphics g) {
		g.setColor(new Color(87,0,127));
		g.drawRect((int)x,(int)y,(int)width,(int)height);
		bubble.render(g);
		nameBox.render(g);
	}

	public Rectangle getBounds() {
		return new Rectangle((int)x,(int)y,(int)width+20,(int)height);
	}

}
