# Creating the Pizza Panic Game

# Import the games and color module from livewires package for creating a game and allowing to choose from a set of colors
from livewires import games, color
import random # for setting the random position of the pizzas

# Initialize the screen and provide access to the games mouse object
games.init(screen_width=640,screen_height=480, fps=50) # fps: Frames per second
# Create a Pan class
class Pan(games.Sprite): # Pan inherits from its super class (Sprite)
	
	# Upload the image of Pan
	pan_pic=games.load_image("pan.jpg") ## Using pan_pic instead of image
	
	# Constructor to initialize new Pan Object with its image, position (x and y)
	def __init__(self): 
		super(Pan,self).__init__(image=Pan.pan_pic, 
								x=games.mouse.x,
								bottom=games.screen.height) ##using y instead of bottom
								
		self.score=games.Text(value=0, color=color.red, size=25, right=games.screen.width-10, top=5) ## Using y instead of top and x instead of right
		games.screen.add(self.score) # The score is always 10 pixels left of the right edge of the screen i.e games.screen.width-10
	
	# Method to move player's pan
	def update(self):
		# start by placing pan in accordance with mouse position
		self.x=games.mouse.x 
		# If pan goes out of left edge then reset the left edge to 0
		if self.left<0:
			self.left=0
		# If Pan goes out of the right edge then reset the right edge to the width of the screen
		if self.right>games.screen.width:
			self.right=games.screen.width
		# Call the check_catch() to see if pan caught any pizza or not
		self.check_catch()
		
	def check_catch(self):
		for pizza in self.overlapping_sprites:
			self.score.value+=10 # Increase the score by 10 
			self.score.right=games.screen.width-10#place the new score again 10 pixels away from the right edge of the screen
			pizza.handle_caught()# Call the Pizza's handle_caught()
			
#Create the Pizza class
class Pizza(games.Sprite):
	
	#Upload the Pizza Image
	pizza_pic=games.load_image("pizza.jpg")
	speed=1 # Falling speed of Pizzas
	
	#set the initial values for the pizza-Constructor
	def __init__(self,x,y=90): # Place the pizza at chef's chest level
		super(Pizza,self).__init__(image=Pizza.pizza_pic, x=x,y=y,dy=Pizza.speed)  
	# Method to check the screen boundary for pizzas
	def update(self):
		if self.bottom > games.screen.height: # if the pizza moves out of the screen then call end_game() and destroy the pizza sprite object; ## Used y instead of bottom
			self.end_game()
			self.destroy()
	def handle_caught(self):
		self.destroy()
		
	def end_game(self):
		# At the end of the game just display the message and destroy the Pizza Sprite
		end_msg=games.Message(value="Game Over!", 
							  color=color.brown,
							  size=90,
							  x=games.screen.width/2,
							  y=games.screen.height/2,
							  lifetime=5*games.screen.fps, # Number of frames in 1 second=5*50=250 so 250/50=5 seconds
							  after_death=games.screen.quit)
		games.screen.add(end_msg)

class Chef(games.Sprite):
	# Upload the Chef's Image
	chef_pic=games.load_image("chef.jpg")
	#Contsructor to initialize the chef
	def __init__(self,y=55, speed=2,odds_change=200):
		super(Chef,self).__init__(image=Chef.chef_pic,
								  x=games.screen.width/2, # Chef is in the middle and on the top of the brick wall
								  y=y,
								  dx=speed) # Chef only moves in the x-direction
								  
		self.odds_change=odds_change # Odds_change is an integer that represents odds that chef will change his direction 
		#e.g if odd_change=200 then there is 1 in 200 chance that chef will change his direction, you will see it's use in update()
		
		self.time_til_drop=0 # It is an integer in mainloop cycles that represents time till chef drop the next pizza. It is set to 0 initially so
		#that when chef spring to life a pizza is immediately dropped. See its use in the check_drop()
		
	#Method that discusses how the Chef moves
	def update(self):
		if self.left <0 or self.right>games.screen.width:
			self.dx=-self.dx
		elif random.randrange(self.odds_change)==0: 
			self.dx=-self.dx
		# This method is called every mainloop cycle-DOES NOT MEAN that: A new pizza is dropped every 50 seconds
		self.check_drop()
		
	def check_drop(self):
		#Countdown for the chef to drop the pizza
		if self.time_til_drop >0:
			self.time_til_drop-=1
		else:
			new_pizza=Pizza(x=self.x) # new pizza created at x position of the Chef Sprite
			games.screen.add(new_pizza)
			self.time_til_drop=int(new_pizza.height*1.3/Pizza.speed)+1 #Next pizza is dropped when the distance from the previous pizza  is about 
			#30% of pizza height, independent of how fast the pizzas are falling 
def main():
	wall_pic=games.load_image("Wall.jpg", transparent=False)
	games.screen.background=wall_pic
	the_chef=Chef()
	games.screen.add(the_chef)
	the_pan=Pan()
	games.screen.add(the_pan)
	games.mouse.is_visible=False
	games.mouse.event_grab=True
	games.screen.mainloop()
		
main()
	
		
		
			
		
		
		

