package com.lieutenantjaku.testing.window;

import java.awt.Graphics;
import java.util.LinkedList;

import com.lieutenantjaku.testing.framework.GameObject;
import com.lieutenantjaku.testing.framework.ObjectId;
import com.lieutenantjaku.testing.objects.Block;
import com.lieutenantjaku.testing.objects.Elevator;

public class Handler {

	public LinkedList<GameObject> object = new LinkedList<GameObject>();
	
	private GameObject tempObject;
	
	public void tick() {
		for (int i =0; i < object.size(); i++) {
			
			tempObject = object.get(i);
			
			tempObject.tick(object);
		}
	}
	
	public void render(Graphics g) {
		for (int i =0; i < object.size(); i++) {
			
			tempObject = object.get(i);
			
			tempObject.render(g);
		}
	}
	
	public void addObject(GameObject object) {
		this.object.add(object);
	}
	public void removeObject(GameObject object) {
		this.object.remove(object);
	}
	
	public LinkedList<GameObject> getList() {
		return object;
	}
	
	public void createLevel() {
		for(int xx = 0; xx < Game.WIDTH+32; xx += 32) {
			addObject(new Block(xx,Game.HEIGHT-32, ObjectId.Block));
		}
		for(int xx = 0; xx < Game.HEIGHT-64; xx += 32) {
			addObject(new Block(Game.WIDTH-32,xx, ObjectId.Block));
		}
		for(int xx = 0; xx < Game.HEIGHT-64; xx += 32) {
			addObject(new Block(0,xx, ObjectId.Block));
		}
		for(int xx = 100; xx < 300; xx += 32) {
			addObject(new Block(xx,400, ObjectId.Block));
		}
		for(int xx = 320; xx < Game.HEIGHT-64; xx += 32) {
			addObject(new Elevator(400,xx, ObjectId.Elevator));
		}
	}
	
}
