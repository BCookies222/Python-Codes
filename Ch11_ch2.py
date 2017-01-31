# WAP where a player controls a character that must avoid falling debris. The player controls the character with the mouse and objects fall from the sky.


from livewires import games, color
import random

games.init(screen_width=600, screen_height=450, fps=50)

class Character(games.Sprite):
	# Load Image of character-bowl
	Char_img=games.load_image("bowl.jpg")
	# Constructor-Bowl will have image, x and y positions
	def __init__(self):
		super(Character,self).__init__(image=Character.Char_img, # Important to add class name before its variable
								       x=games.mouse.x, # set the character at mouse position
								       bottom=games.screen.height) # y coodinate of the bottom sprite edge
									   
		# Add text for score-Text will be 10 pixels away from screen.width
		self.score=games.Text(value=0,color=color.red, size=50,right=games.screen.width-10, top=10)
		games.screen.add(self.score)
		
	
	# Method to move player's character-bowl
	def update(self):
		# start by placing bowl in accordance with mouse position
		self.x=games.mouse.x #? Why not using right instead of x 
		# If bowl goes out of left edge then reset the left edge to 0
		if self.left<0: # Update method has left and right properties
			self.left=0
		# If bowl goes out of the right edge then reset the right edge to the width of the screen
		if self.right>games.screen.width:
			self.right=games.screen.width
		# Call the check_catch() to see if bowl caught any pearl or not
		self.check_catch()
		
	def check_catch(self):
		for d in self.overlapping_sprites:
			
			if Debris.debris: # if debris are falling
				self.score.value+=10 # Increase the score by 10 
				self.score.right=games.screen.width-10#place the new score again 10 pixels away from the right edge of the screen
				# Catch the debris
				Debris.debris_handle_caught(self)# Call the Debris handle_caught()
			if Pearl.debris: # No debris
				self.score.value=0
				Pearl.pearl_handle_caught(self)
			
#Create the Pearls class
class Pearl(games.Sprite):
	
	#Upload the Pink pearl and debris  Image
	pinkpearl_img=games.load_image("pinkpearl.jpg")
	pink_speed=2 # Falling speed of pearls
	debris=False
	#set the initial values for the  pearl-Constructor(i.e pearl will have x and y positions)
	def __init__(self,x_pink=2,y_pink=90): # Place the pearls at Cloud's chest level 
		super(Pearl,self).__init__(image=Pearl.pinkpearl_img,x=x_pink,y=y_pink,dy=Pearl.pink_speed) 
		
	def pearl_handle_caught(self):	
		pass
		
class Debris(games.Sprite):

	debris_img=games.load_image("debris.jpg")
	debris=True
	debris_speed=2
	def __init__(self,x_debris=10,y_debris=90): # Place the debris at Cloud's chest level ?? Not clear its not defined in angles
		super(Debris,self).__init__(image=Debris.debris_img,x=x_debris,y=y_debris,dy=Debris.debris_speed) 
	# Method to check the screen boundary for pearls
	def update(self):
		if self.bottom > games.screen.height: # if the pearl moves out of the screen then call end_game() and destroy the pearl sprite object; 
			self.end_game()
			self.destroy()
	def debris_handle_caught(self):
		self.destroy()
		
	def end_game(self):
		# At the end of the game just display the message and destroy the pearl Sprite
		end_msg=games.Message(value="Game Over!", 
							  color=color.black,
							  size=90,
							  x=games.screen.width/2, # Message has x and y, lifetime and after_death
							  y=games.screen.height/2,
							  lifetime=5*games.screen.fps, # Number of frames in 1 second=5*50=250 so 250/50=5 seconds
							 # after_death=games.screen
							 )
		games.screen.add(end_msg)
				
		
class Cloud_pearl(games.Sprite):
	cloud_img=games.load_image("cloud.png", transparent=False)
	def __init__(self,y=10, speed=3,odds_change=200):
		super(Cloud_pearl,self).__init__(image=Cloud_pearl.cloud_img,
								  x=games.screen.width/2, # Cloud is in the middle and on the top of the brick wall
								  y=y,
								  dx=speed) # Cloud only moves in the x-direction
								  
		self.odds_change=odds_change # Odds_change is an integer that represents odds that Cloud will change his direction 
		#e.g if odd_change=200 then there is 1 in 200 chance that Cloud will change his direction, you will see it's use in update()
		
		self.time_til_drop=0 # It is an integer in mainloop cycles that represents time till Cloud drop the next pearl. It is set to 0 initially so
		#that when Cloud spring to life a pearl is immediately dropped. See its use in the check_drop()
		
	#Method that discusses how the Cloud moves
	def update(self):
		if self.left <0 or self.right>games.screen.width:
			self.dx=-self.dx
		elif random.randrange(self.odds_change)==0: # what is meant by this statement- help cloud move in reverse direction suddenly;  making game interesting
			self.dx=-self.dx
		# This method is called every mainloop cycle-DOES NOT MEAN that: A new pearl is dropped every 50 seconds
		self.check_drop()
		
	def check_drop(self):# ?
		#Countdown for the Cloud to drop the pearl
		if self.time_til_drop>0:
			self.time_til_drop-=1 
		else:
			new_pinkpearl=Pearl(x_pink = self.x) # new pearl created at x position of the Cloud Sprite
			games.screen.add(new_pinkpearl)
			self.time_til_drop=int(new_pinkpearl.height*2/Pearl.pink_speed)+1 #Next pearl is dropped when the distance from the previous pearl  is about 
			#30% of pearl height, independent of how fast the pearls are falling -??? Should I  change no. of pearls here by changing the %	
			
class Cloud_debris(games.Sprite):
	cloud_img=games.load_image("cloud.png", transparent=False)
	def __init__(self,y=10, speed=2,odds_change=500):
		super(Cloud_debris,self).__init__(image=Cloud_debris.cloud_img,
								  x=games.screen.width/4, # Cloud is in the middle and on the top of the brick wall
								  y=y,
								  dx=speed) # Cloud only moves in the x-direction
								  
		self.odds_change=odds_change # Odds_change is an integer that represents odds that Cloud will change his direction 
		#e.g if odd_change=200 then there is 1 in 200 chance that Cloud will change his direction, you will see it's use in update()
		
		self.time_til_drop=0 # It is an integer in mainloop cycles that represents time till Cloud drop the next pearl. It is set to 0 initially so
		#that when Cloud spring to life a pearl is immediately dropped. See its use in the check_drop()
		
	#Method that discusses how the Cloud moves
	def update(self):
		if self.left <0 or self.right>games.screen.width:
			self.dx=-self.dx
		elif random.randrange(self.odds_change)==0: # ? what is meant by this statement
			self.dx=-self.dx
		# This method is called every mainloop cycle-DOES NOT MEAN that: A new pearl is dropped every 50 seconds
		self.check_drop()
		
	def check_drop(self):
		#Countdown for the Cloud to drop the pearl
		if self.time_til_drop >0:
			self.time_til_drop-=1 
		else:
			
			new_debris=Debris(x_debris=self.x) # new debris created at x position of the Cloud Sprite
			games.screen.add(new_debris)
			self.time_til_drop=int(new_debris.height*1.6/Debris.debris_speed)+1 #?



def main():
	Valley_Img=games.load_image("valley.jpg", transparent=False)
	games.screen.background=Valley_Img
	
	the_char=Character()
	games.screen.add(the_char)
	
	the_pearl=Pearl()
	games.screen.add(the_pearl)
	
	the_debris=Debris()
	games.screen.add(the_debris)
	
	the_cloud_pearl=Cloud_pearl()
	games.screen.add(the_cloud_pearl)
	
	the_cloud_debris=Cloud_debris()
	games.screen.add(the_cloud_debris)
	
	games.mouse.is_visible=True
	games.mouse.event_grab=True
	
	
	
	games.screen.mainloop()
	print (the_char.score.value)
	

main()

	
	
		
									   
									   
									   
									   
	
