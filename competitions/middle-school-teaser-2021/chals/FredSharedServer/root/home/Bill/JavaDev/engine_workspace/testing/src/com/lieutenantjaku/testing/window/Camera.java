package com.lieutenantjaku.testing.window;

import com.lieutenantjaku.testing.framework.GameObject;

public class Camera {

	private float x,y;
	
	public Camera(float x, float y) {
		this.x = x;
		this.y = y;
	}
	public void setX(float x) {
		this.x = x;
	}
	public void setY(float x) {
		this.y = y;
	}
	public float getX() {
		return x;
	}
	public float getY() {
		return y;
	}
	public void tick(GameObject Player) {
		x= -Player.getX()+Game.WIDTH/2;
		y= -Player.getY()+Game.WIDTH/2;
	}
	
}
