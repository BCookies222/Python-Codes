# Handling Collision

from livewires import games,color
import random

#Initialize screen and initialize mouse position for pan
games.init(screen_width=640, screen_height=480, fps=50)

#Create a Pan class
class Pan(games.Sprite):
	def update(self): # Update x and y and check for collison on every mainloop run
		self.x=games.mouse.x
		self.y=games.mouse.y
		self.check_collision()
		
	def check_collision(self):
		for pizza in self.overlapping_sprites: # overlapping_sprites is a property of a sprite (Pan here) that would check if the mentioned(pizza) sprite overlaps it or not
			pizza.handle_collide()

#Create a Pizza class		
class Pizza(games.Sprite):
	def update(self):
		if self.right>games.screen.width or self.left<0:
			self.dx=-self.dx
		if self.bottom >games.screen.height or self.top<0:
			self.dy=-self.dy
	def handle_collide(self):
		#Move the pizza to new position as soon as the pan is near the /colliding with the pizza
		self.x=random.randrange(games.screen.width)
		self.y=random.randrange(games.screen.height)
	
	
	
def main():
	
	# load the wall image
	wall_img=games.load_image("Wall.jpg", transparent=False)
	# add the wall to screen background
	games.screen.background=wall_img
	# The following Text and Message are not included in this code because they need special handling because the pan collides with them and generates an error 
	"""# create a Text 
	txt=games.Text(value="1256734",color=color.pink, size=30, x=550,y=30)
	# add the text to the screen
	games.screen.add(txt)
	
	#create a message
	msg=games.Message(value="You Won!", 
					  size=30, 
					  color=color.brown,
					  x=games.screen.width/2, 
					  y=games.screen.height/2, 
					  lifetime=1500, 
					  after_death=games.screen.quit)
	# add the message to the screen
	games.screen.add(msg)"""
	
	# load the pizza Image
	pizza_pic=games.load_image("pizza.jpg")
	pizza_img=Pizza(image=pizza_pic, 
					x=random.randrange(games.screen.width), 
					y=random.randrange(games.screen.height),
					dx=1, 
					dy=1)
					
	# Add the pizza image to the screen
	games.screen.add(pizza_img)

	#Load the pan image
	pan_pic=games.load_image("pan.jpg")
	pan_img=Pan(image=pan_pic, 
				x=games.mouse.x,
				y=games.mouse.y)
	# Add the pan image to the screen
	games.screen.add(pan_img)
	
	games.mouse.is_visible=False
	
	games.screen.event_grab=True

	games.screen.mainloop()


main()

	
		
	

