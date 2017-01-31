# Setting the mouse pointer

from livewires import games,color
#Initialize the screen and MOUSE object-Important
games.init(screen_width=640, screen_height=480, fps=50)

#create a class for Pan
# with every mainloop() pan and pizza positions update
class Pan(games.Sprite):
	def update(self):
		self.x=games.mouse.x # assign the pan's x position to the current mouse position
		self.y=games.mouse.y
class Pizza(games.Sprite):
	def update(self):
		if self.right>games.screen.width or self.left<0:
			self.dx=-self.dx
		if self.bottom > games.screen.height or self.top<0:
			self.dy=-self.dy
		

def main():
	
	
	#Load the wall image
	wall_pic=games.load_image("Wall.jpg", transparent=False)
	#Set the screen background
	games.screen.background=wall_pic
	
	#Upload the pan image 
	pan_pic=games.load_image("pan.jpg")
	
	#Setting the position of pan initially
	pan_img=Pan(image=pan_pic,
				x=games.mouse.x,
				y=games.mouse.y)
	#Add pan to screen
	games.screen.add(pan_img)
	#Set the visibility of the mouse
	games.mouse.is_visible=False
	#Grab the mouse on the screen-i.e the mouse will only reply to click within the screen and not outside. For closing the screen you need to press ESC
	games.screen.event_grab=True
	
	#Upload the pizza image
	pizza_pic=games.load_image("pizza.jpg")
	#Setting the position of pizza initially
	pizza_img=Pizza(image=pizza_pic,    
					x=games.screen.width/2,
					y=games.screen.height/2,
					dx=1,
					dy=1)
	#Add pizza to screen				
	games.screen.add(pizza_img)
	
	#Create a text
	txt=games.Text(value="1257648", size=30, color=color.pink, x=550, y=30)
	# add text to screen
	games.screen.add(txt)
	
	
	#Create a message
	msg=games.Message(value="You Won!", size=30, color=color.brown, x=games.screen.width/2, y=games.screen.height/2, lifetime=1500, after_death=games.screen.quit)
	#Add the message to the screen
	games.screen.add(msg)
	
	games.screen.mainloop()
	
	
	
main()
	
	
	
