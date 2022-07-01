package com.lieutenantjaku.testing.objects;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.util.LinkedList;

import com.lieutenantjaku.testing.framework.GameObject;
import com.lieutenantjaku.testing.framework.KeyInput;
import com.lieutenantjaku.testing.framework.ObjectId;
import com.lieutenantjaku.testing.window.Handler;

public class Enemy extends GameObject{
	
	private float width = 48, height = 48;
	private float gravity = 0.2f;
	private final float MAX_SPEED = 10;
	private Handler handler;
	int countX = 0;
	int countY = 0;
	private int direction;
	private int enemyId=0;
	private static int idCount=0;
	private double health;
	
	public Enemy(float x, float y, Handler handler,ObjectId id, KeyInput input,int updown,int hits) {
		super(x, y, id);
		this.handler = handler;
		direction=updown;
		enemyId=idCount;
		health=10*hits;
		idCount++;
	}
	KeyInput input = (new KeyInput(handler));
	public void tick(LinkedList<GameObject> object) {
		x += velX;
		y += velY;
		if(countX<=200){
			velX=2;
		}
		if(countX>200){
			velX=-2;
			if(countX>400){
				countX=0;
			}
		}
		Collision(object);
		if(falling || jumping) {
			if (velY > MAX_SPEED){
				velY = MAX_SPEED;
			}
			
		}
		if (health<=0) {
			System.out.println("DEAD");
			alive = false;
			for(int i =0; i< handler.object.size(); i++) {
				GameObject tempObject = handler.object.get(i);
					if (tempObject.getId()== ObjectId.Enemy) {
						if(tempObject instanceof Enemy) {
							if(((Enemy) tempObject).getEnemyId()==enemyId) {
								handler.removeObject(tempObject);
							}
						}
					}
				}
		}
		if (jumping) {
			height = 96;
		}
		countX++;
	}
	
	private void Collision(LinkedList<GameObject> object) {
		for(int i =0; i< handler.object.size(); i++) {
		GameObject tempObject = handler.object.get(i);
			if (tempObject.getId()== ObjectId.Block) {
				if(getBounds().intersects(tempObject.getBounds())) {
					y = tempObject.getY() + (32);
					velY = 0;
				}
			}
			if (tempObject.getId()== ObjectId.Bullet) {
				if(getBounds().intersects(tempObject.getBounds())) {
					health-=10;
					System.out.println(health);
					handler.removeObject(tempObject);
				}
			}
		}
	}
	
	public void render(Graphics g) {
		g.setColor(Color.orange);
		g.drawRect((int)x,(int)y,(int)width,(int)height);
		
		/*Graphics2D g2d = (Graphics2D) g;
		g.setColor(Color.red);
		g2d.draw(getBounds());
		g2d.draw(getBoundsRight());
		g2d.draw(getBoundsLeft());
		g2d.draw(getBoundsTop());*/
	}
	public int getEnemyId() {
		return enemyId;
	}
	public float getVelX() {
		return velX;
	}
	public float getVelY() {
		return velY;
	}
	public float getY() {
		return y;
	}
	public float getX() {
		return x;
	}
	public float getScore() {
		return score;
	}
	public Rectangle getBounds() {
		return new Rectangle((int)x,(int)y,(int)width,(int)height);
	}
}
