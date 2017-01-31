# Adding Sound and Music to the Animation

from livewires import games, color

games.init(screen_width=640, screen_height=480, fps=50)

"""class Ship(games.Sprite):
	def update(self):
		if games.keyboard.is_pressed(games.K_w):
			self.y=self.y-1
		if games.keyboard.is_pressed(games.K_s):
			self.y=self.y+1	
		if games.keyboard.is_pressed(games.K_a):
			self.x=self.x-1
		if games.keyboard.is_pressed(games.K_d):
			self.x=self.x+1	
		if games.keyboard.is_pressed(games.K_LEFT):
			self.angle=self.angle-1
		if games.keyboard.is_pressed(games.K_RIGHT):
			self.angle+=1
		if games.keyboard.is_pressed(games.K_1):
			self.angle=0
		if games.keyboard.is_pressed(games.K_2):
			self.angle=90
		if games.keyboard.is_pressed(games.K_3):
			self.angle=180
		if games.keyboard.is_pressed(games.K_4):
			self.angle=270"""
			
#def main():
"""nebula=games.load_image("nebula.jpg",transparent=False)
games.screen.background=nebula"""

"""ship_pic=games.load_image("ship.bmp")
the_ship=Ship(image=ship_pic,
			  x=games.screen.width/2,
			  y=games.screen.height/2)
games.screen.add(the_ship)
	
# Add the list of pics to be animated
explosion_images=["explosion1.bmp",
				  "explosion2.bmp",
				  "explosion3.bmp",
				  "explosion4.bmp",
				  "explosion5.bmp",
				  "explosion6.bmp",
				  "explosion7.bmp",
				  "explosion8.bmp",
				  "explosion9.bmp",
					]
explosion=games.Animation(images=explosion_images, # list of images
						  x=games.screen.width/2,
						  y=games.screen.height/2,
						  n_repeats=0, # Forever
						  repeat_interval=5
							  )
games.screen.add(explosion)"""
	
# Sound-load(), play(), stop()
# Load the SOUND File load_sound will only take WAV files, will be loaded with games.load_sound and create object
missile_sound=games.load_sound("missile.wav") # Waveform Audio File Format (WAVE, or more commonly known as WAV due to its filename extension)(rarely, Audio for Windows)is a #Microsoft and IBM audio file format standard for storing an audio bitstream on PCs.
	
# Load the MUSIC File
games.music.load("theme.mid") #MIDI (/ˈmɪdi/; short for Musical Instrument Digital Interface) is a technical standard that describes a protocol, digital interface and #connectors #and allows a wide variety of electronic musical instruments, computers and other related devices to connect and communicate with one another
	
# Play the Sound
choice=None
while choice!=0:		
	print (""" 
		       0-QUIT
			   1-Play the missile sound
			   2-Loop the missile sound
			   3-Stop the missile sound
			   4-Play the theme music,
			   5-Loop the theme music,
			   6-Stop the theme music""")
			   
	choice=int(input("Enter the choice: "))
	print()
	
	if choice==0:
		print("Good-bye")
		exit()
	elif choice==1:
		missile_sound.play() # Sound can be played on one of the 8 channels
		print("Playing the missile sound")
	elif choice==2:
		loop=int(input("Enter the additional number of times you want to listen to the sound"))
		missile_sound.play(loop) # Atleast loops once so give additional number to be looped (besides once) in the () i.e if loop=3 , sound will be played 1+3=4 times
		print("Looping the missile sound")
	elif choice==3:
		missile_sound.stop()
		print("Stopping the missile sound")
	
	# 1. Music can be played on only 1 channel(so do not create a new object for each music file, instead access the load, play and stop ()) 
	# 2. Music can accept many file formats like WAV, MIDI, MP3, OGG
	elif choice==4:
		games.music.play()
		print("Playing the theme music")
	elif choice==5:
		loop=int(input("Enter the additional number of times you want to listen to the theme music"))
		games.music.play(loop) # if loop=x then music will be played x+1 times
		print("Looping the theme music")
	elif choice==6:
		games.music.stop()
		print("Stopping the theme music")
	else:
		print("Sorry!The choice isnt a valid choice")
	
input("\n Press Enter key to exit")
	
#games.screen.mainloop()

	
#main()
	
	