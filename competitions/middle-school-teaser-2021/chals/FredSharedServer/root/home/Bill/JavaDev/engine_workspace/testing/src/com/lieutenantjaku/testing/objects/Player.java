package com.lieutenantjaku.testing.objects;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.util.LinkedList;

import com.lieutenantjaku.testing.framework.ArrayMethods;
import com.lieutenantjaku.testing.framework.GameObject;
import com.lieutenantjaku.testing.framework.KeyInput;
import com.lieutenantjaku.testing.framework.ObjectId;
import com.lieutenantjaku.testing.window.Handler;
import com.lieutenantjaku.testing.objects.TalkingAI;

public class Player extends GameObject{
	
	private float width = 48, height = 96;
	private float gravity = 0.2f;
	private final float MAX_SPEED = 10;
	private Handler handler;
	private boolean canLeave = false;
	private ArrayMethods function=new ArrayMethods();
	private Coin coin=new Coin(64,64,ObjectId.Coin);
	private int timer=0;
	private static int idCount=0;
	private int playerId;
	
	public Player(float x, float y, Handler handler,ObjectId id, KeyInput input) {
		super(x, y, id);
		this.handler = handler;
		playerId=idCount;
		idCount++;
	}
	KeyInput input = (new KeyInput(handler));
	public void tick(LinkedList<GameObject> object) {
		x += velX;
		y += velY;
	
		if(falling || jumping) {
			velY += gravity;
			if (velY > MAX_SPEED){
				velY = MAX_SPEED;
			}
			
		}
		Collision(object);
		if (health<=0) {
			alive = false;
			for(int i =0; i< handler.object.size(); i++) {
				GameObject tempObject = handler.object.get(i);
				if (tempObject instanceof Player) {
					if(((Player)tempObject).getPlayerId()==playerId){
						handler.addObject(new GameOver((float)x,(float)y,handler,ObjectId.GameOver));
						handler.removeObject(tempObject);
					}
				}
			}
		}
		if (alive == false){
			velX=0;
			velY=0;
		}
		if (jumping) {
			height = 96;
		}
		if (timer ==50) {
			if (function.checkAmount(handler.getList(), coin)==0) {
				canLeave=true;
			}
			timer=0;
		}
		timer++;
	}

	private void Collision(LinkedList<GameObject> object) {
	
		for(int i =0; i< handler.object.size(); i++) {
			GameObject tempObject = handler.object.get(i);
			if (tempObject.getId()== ObjectId.Block) {
				if(getBoundsTop().intersects(tempObject.getBounds())) {
					y = tempObject.getY() + (32);
					velY = 0;
				}
				if(getBounds().intersects(tempObject.getBounds())) {
					y = tempObject.getY() - height;
					velY = 0;
					falling = false;
					jumping = false;
					if (Spress == true) {
						height =48;
					}
					else {
						height = 96;
					}
				}
				if(getBoundsRight().intersects(tempObject.getBounds())) {
					x = tempObject.getX() - (width+2);
					velX = 0;
					if (Dpress == true) {
						velX=5;
					}
				}
				if(getBoundsLeft().intersects(tempObject.getBounds())) {
					x = tempObject.getX() + (34);
					velX = 0;
					if (Apress == true) {
						velX=-5;
					}
				}
				else {
					falling = true;
				}
			}
			if (tempObject.getId()== ObjectId.Elevator) {
				if(getBounds().intersects(tempObject.getBounds())) {
					velY+= -.25;
					jumping = false;
				}
				else {
						falling = true;
					
				}
			}
			if (tempObject.getId()== ObjectId.Coin) {
				if(getBounds().intersects(tempObject.getBounds())) {
				score++;
				System.out.println(score);
				handler.removeObject(tempObject);
				}
				if(getBoundsTop().intersects(tempObject.getBounds())) {
					score++;
					System.out.println(score);
					handler.removeObject(tempObject);
					}
				if(getBoundsLeft().intersects(tempObject.getBounds())) {
					score++;
					System.out.println(score);
					handler.removeObject(tempObject);
					}
				if(getBoundsRight().intersects(tempObject.getBounds())) {
					score++;
					System.out.println(score);
					handler.removeObject(tempObject);
					}
			}
			if (tempObject.getId()== ObjectId.ExitGate) {
				if (canLeave) {
					handler.removeObject(tempObject);
				}
				else {
					if(getBoundsTop().intersects(tempObject.getBounds())) {
						y = tempObject.getY() + (32);
						velY = 0;
					}
					if(getBounds().intersects(tempObject.getBounds())) {
						y = tempObject.getY() - height;
						velY = 0;
						falling = false;
						jumping = false;
						if (Spress == true) {
							height =48;
						}
						else {
							height = 96;
						}
					}
					if(getBoundsRight().intersects(tempObject.getBounds())) {
						x = tempObject.getX() - (width+2);
						velX = 0;
						if (Dpress == true) {
							velX=5;
						}
					}
					if(getBoundsLeft().intersects(tempObject.getBounds())) {
						x = tempObject.getX() + (34);
						velX = 0;
						if (Apress == true) {
							velX=-5;
						}
					}
					else {
						falling = true;
					}
				}
			}
			if (tempObject.getId()== ObjectId.Damage||tempObject.getId()==ObjectId.Enemy) {
				if(getBounds().intersects(tempObject.getBounds())) {
					health-=0.5;
					//System.out.println(health);
				}
				if(getBoundsTop().intersects(tempObject.getBounds())) {
					health-=0.5;
					//System.out.println(health);
				
				}
			}
			if (tempObject.getId()== ObjectId.Person1) {
				if(getBounds().intersects(tempObject.getBounds())) {
					if(Epress) {
							try {
								((TalkingAI) tempObject).speech();
								Thread.sleep(1000);
							} catch (InterruptedException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}

					}
				}
			}
		}
	}
	public float getHealth(){
		return health;
	}
	public void render(Graphics g) {
		g.setColor(Color.blue);
		g.drawRect((int)x,(int)y,(int)width,(int)height);	
	
		
		/*Graphics2D g2d = (Graphics2D) g;
		g.setColor(Color.red);
		g2d.draw(getBounds());
		g2d.draw(getBoundsRight());
		g2d.draw(getBoundsLeft());
		g2d.draw(getBoundsTop());*/
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
	public int getPlayerId() {
		return playerId;
	}
	public float getScore() {
		return score;
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
