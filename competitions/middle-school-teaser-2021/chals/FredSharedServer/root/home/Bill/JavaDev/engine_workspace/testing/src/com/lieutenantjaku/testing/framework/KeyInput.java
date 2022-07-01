package com.lieutenantjaku.testing.framework;

import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

import com.lieutenantjaku.testing.objects.Bullet;
import com.lieutenantjaku.testing.window.Handler;

public class KeyInput extends KeyAdapter{
	
	Handler handler;
	// 1 is R
	// -1 is L
	
	public KeyInput(Handler handler) {
		this.handler = handler;
	}
	
	public void keyPressed(KeyEvent e) {
		int key = e.getKeyCode();
		
		for(int i = 0; i < handler.object.size(); i++) {
			GameObject tempObject = handler.object.get(i);
			if (tempObject.getId()== ObjectId.Player) {
				if (key == KeyEvent.VK_D||key==KeyEvent.VK_RIGHT) {
					tempObject.setVelX(5);
					tempObject.setDpress(true);
					tempObject.setFacing(1);
				}
				if (key == KeyEvent.VK_A||key==KeyEvent.VK_LEFT) {
					tempObject.setVelX(-5);
					tempObject.setApress(true);
					tempObject.setFacing(-1);
				}
				if ((key == KeyEvent.VK_W ||key==KeyEvent.VK_UP)&& !tempObject.isJumping()) {
					tempObject.setJumping(true);
					tempObject.setVelY(-10);
				}
				if (key == KeyEvent.VK_S||key==KeyEvent.VK_DOWN) {
					tempObject.setVelY(5);
					tempObject.setSpress(true);
				}
				if (key==KeyEvent.VK_SPACE) {
					handler.addObject(new Bullet(tempObject.getX(),tempObject.getY(),ObjectId.Bullet, tempObject.getFacing()*5));
				}
				if (key == KeyEvent.VK_E) {
					tempObject.setEpress(true);
				}
			}
		}
		
		if (key == KeyEvent.VK_ESCAPE) {
			System.exit(1);
		}
	}

	public void keyReleased(KeyEvent e) {
		int key = e.getKeyCode();
		
		for(int i = 0; i < handler.object.size(); i++) {
			GameObject tempObject = handler.object.get(i);
			if (tempObject.getId()== ObjectId.Player) {
				if (key == KeyEvent.VK_D||key==KeyEvent.VK_RIGHT) {
					tempObject.setVelX(0);
					tempObject.setDpress(false);
					
				}
				if (key == KeyEvent.VK_A||key==KeyEvent.VK_LEFT) {
					tempObject.setVelX(0);
					tempObject.setApress(false);
				}
				if (key == KeyEvent.VK_W||key==KeyEvent.VK_UP) tempObject.setVelY(0);
				if (key == KeyEvent.VK_S||key==KeyEvent.VK_DOWN) {
					tempObject.setVelY(0);
					tempObject.setSpress(false);
				}
				if (key == KeyEvent.VK_E) {
					tempObject.setEpress(false);
				}
			}
		}
		
	}
	
}
