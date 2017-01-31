#Space Ship and its motion-Linear and Rotational with keys
# Showing explosion as Animation

from livewires import games, color

games.init(screen_width=640, screen_height=480, fps=50)

class Ship(games.Sprite):
	# Update method tells how the shop moves and rotates
	def update(self): # Use keyboard object and its is_pressed() and use games.K_ constants for keys
		if games.keyboard.is_pressed(games.K_w): # Check if key W is pressed return True if it is or False if it isnt
			self.y=self.y-1
		if games.keyboard.is_pressed(games.K_s): # Check if key S is pressed return True if it is or False if it isnt
			self.y=self.y+1
		if games.keyboard.is_pressed(games.K_a): # Check if key A is pressed return True if it is or False if it isnt
			self.x=self.x-1
		if games.keyboard.is_pressed(games.K_d): # Check if key D is pressed return True if it is or False if it isnt
			self.x=self.x+1	
		if games.keyboard.is_pressed(games.K_RIGHT): # Check if Right Arrow Key is pressed return True if it is or False if it isnt
			self.angle=self.angle+1 #Clockwise
		if games.keyboard.is_pressed(games.K_LEFT): # Check if Left Arrow key is pressed return True if it is or False if it isnt
			self.angle-=1
		if games.keyboard.is_pressed(games.K_1): # Check if key 1 is pressed return True if it is or False if it isnt
			self.angle=0
		if games.keyboard.is_pressed(games.K_2): # Check if key 2 is pressed return True if it is or False if it isnt
			self.angle=90
		if games.keyboard.is_pressed(games.K_3): # Check if key 3 is pressed return True if it is or False if it isnt
			self.angle=180
		if games.keyboard.is_pressed(games.K_4): # Check if key 1 is pressed return True if it is or False if it isnt
			self.angle=270	
		
								 
			
			
				
def main():
	nebula_img=games.load_image("nebula.jpg", transparent=False)
	games.screen.background=nebula_img
	
	ship_pic=games.load_image("ship.bmp")
	the_Ship=Ship(image=ship_pic,
				  x=games.screen.width/2,
				  y=games.screen.height/2 )
				  
	explosion_images=["explosion1.bmp", #List_of _strings_images
								 "explosion2.bmp",
								 "explosion3.bmp",
								 "explosion4.bmp",
								 "explosion5.bmp",
								 "explosion6.bmp",
								 "explosion7.bmp",
								 "explosion8.bmp",
								 "explosion9.bmp"]
				  
	explosion=games.Animation(images=explosion_images, # Very imp: "images" 
							  x=games.screen.width/2,
							  y=games.screen.height/2,
							  n_repeats=0,# Loop forever-Default Value
							  repeat_interval=5) # Frames repeat after delay of 5, Higher number means slow animation and vice versa
	
	games.screen.add(explosion)						  
	games.screen.add(the_Ship)
	
	games.screen.mainloop()
	

main()	
	
