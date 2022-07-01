package com.lieutenantjaku.testing.framework;

import java.awt.Graphics;
import java.awt.Rectangle;
import java.util.LinkedList;

public abstract class GameObject {

	protected float x, y;
	protected float velX =0, velY = 0;
	protected ObjectId id;
	protected boolean falling = true;
	protected boolean jumping = false;
	protected boolean Dpress = false;
	protected boolean Apress = false;
	protected boolean Spress = false;
	protected boolean Epress = false;
	protected int score = 0;
	protected float health = 100;
	protected boolean alive=true;
	protected int facing=1;
	
	public GameObject(float x, float y, ObjectId id) {
		
		this.x = x;
		this.y = y;
		this.id = id;
		
	}
	
	public abstract void tick(LinkedList<GameObject> object); 
	public abstract void render(Graphics g);
	public abstract Rectangle getBounds();
	
	public float getX() {
		return x;
	}
	public float getY() {
		return y;
	}
	public void setX(float x) {
		this.x = x;
	}
	public void setY(float y) {
		this.y = y;
	}
	
	public float getVelX() {
		return velX;
	}
	public float getVelY() {
		return velY;
	}
	public void setVelX(float velX) {
		this.velX = velX;
	}
	public void setVelY(float velY) {
		this.velY = velY;
	}
	
	
	public boolean isFalling() {
		return falling;
	}
	public boolean isDpress() {
		return Dpress;
	}
	public boolean isApress() {
		return Apress;
	}
	public boolean isSpress() {
		return Spress;
	}

	public boolean isEpress() {
		return Epress;
	}
	
	public void setFalling(boolean falling) {
		this.falling = falling;
	}
	
	public void setDpress(boolean Dpress) {
		this.Dpress = Dpress;
	}
	
	public void setSpress(boolean Spress) {
		this.Spress = Spress;
	}

	public void setEpress(boolean Epress) {
		this.Epress = Epress;
	}
	
	public void setApress(boolean Apress) {
		this.Apress = Apress;
	}
	
	public boolean isJumping() {
		return jumping;
	}
	
	public int getFacing() {
		return facing;
	}

	public void setFacing(int facing) {
		this.facing = facing;
	}
	
	public void setJumping(boolean jumping) {
		this.jumping = jumping;
	}

	public ObjectId getId() {
		return id;
	}
	
}
