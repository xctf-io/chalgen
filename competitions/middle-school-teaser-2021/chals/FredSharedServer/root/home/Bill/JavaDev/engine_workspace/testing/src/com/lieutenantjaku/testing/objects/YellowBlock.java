package com.lieutenantjaku.testing.objects;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.util.LinkedList;

import com.lieutenantjaku.testing.framework.GameObject;
import com.lieutenantjaku.testing.framework.ObjectId;

public class YellowBlock extends GameObject{

	public YellowBlock(float x, float y, ObjectId id) {
		super(x, y, id);
	}

	public void tick(LinkedList<GameObject> object) {
		
	}

	public void render(Graphics g) {
		g.setColor(new Color(253,238,33));
		g.drawRect((int)x, (int)y, 32, 32);
	}

	
	public Rectangle getBounds() {
		return new Rectangle((int)x,(int)y,32,32);
	}


}
