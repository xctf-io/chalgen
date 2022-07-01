package com.lieutenantjaku.testing.objects;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.util.LinkedList;

import com.lieutenantjaku.testing.framework.GameObject;
import com.lieutenantjaku.testing.framework.ObjectId;

public class Exit extends GameObject{

	public Exit(float x, float y, ObjectId id) {
		super(x, y, id);
	}

	public void tick(LinkedList<GameObject> object) {
		
	}

	public void render(Graphics g) {
		g.setColor(Color.getHSBColor(77, 100, 100));
		g.drawRect((int)x, (int)y, 32, 64);
	}

	
	public Rectangle getBounds() {
		return new Rectangle((int)x,(int)y,32,64);
	}


}
