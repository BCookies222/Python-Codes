#The Astrocrash game
"""This game will have features like
	1. Ship
		It should rotate and thurst forward based on keystrokes from player
		It should fire missiles based on keystroke from the player
		Wrap arpund screen- That is if boundary crossed then appear at the opposite boundary
		If Ship is destroyed GAME IS OVER
		Assets-mage file, sound file for thrust
	2. Missile
		Wrap arpund screen- That is if boundary crossed then appear at the opposite boundary
		If a missile hits another object on the screen it shpud destroy the object and itself in a EXPLOSION
		Assets-Image and Sound file 
		
	3. Asteroids
		There are three types of asteroids-Small, Medium and Large
		Smaller should move faster than Larger ones
		Wrap arpund screen- That is if boundary crossed then appear at the opposite boundary
		If a Large Asteroid is destroyed 2 medium size asteroids are produced and if a Medium Size asteroid is destroyed then two small sized asteroids are produced and 
		if a small asteroid is destroyed then no new asteroids are produced
		If a small asteroid is destroyed player earn more points than if he destroys a larger one
		Once all the astreroids are destroyed new LARGER wave of asteroids is created
		Assets-Images for Smaller. Med and Larger Asteroids, Sound File for Asteroids
*Player's score should be displayed on the upper right corner of the screen
		
	4. Explosion
		Assets-Series of image files for the explosion, Sound file for the explosion, Theme music"""
		
from livewires import games, color
import random, math # Calculate the velocity of ship

games.init(screen_width=640, screen_height=480, fps=50)


class Wrapper(games.Sprite): # This class will wrap the sprites around the screen and a die method to destroy the objects
	def update(self):
		# Wrap  around the screen
		if self.top>games.screen.height:
			self.bottom=0
		if self.bottom<0:
			self.top=games.screen.height
		if self.left>games.screen.width:
			self.right=0
		if self.right<0:
			self.left=games.screen.width

	def die(self): # This die method will be called in Collider class's update method
		self.destroy()

"""Here I invoke its superclass’s update() method (which is Wrapper’s update() method) to keep the object on the screen. Then I check for collisions. If the object overlaps any others, I call the die() method for the other objects and then the object’s own die() method"""
class Collider(Wrapper):
	def update(self):
		super(Collider, self).update()
		if self.overlapping_sprites:
			for sprite in self.overlapping_sprites:
				sprite.die() # See its code above
			self.die() # See its definition below

	# Creating a die() method for the class, since all Collider objects will do the same thing when they die—create an explosion and destroy themselves
	def die(self):
		""" Destroy self and leave explosion behind. """
		new_explosion = Explosion(x = self.x, y = self.y)
		games.screen.add(new_explosion)
		self.destroy()

class Asteroid(Wrapper):
	#class CONSTANTS
	SMALL=1
	MEDIUM=2
	LARGE=3
	images={SMALL:games.load_image("asteroid_small.bmp"),
			MEDIUM:games.load_image("asteroid_med.bmp"),
			LARGE:games.load_image("asteroid_big.bmp")}
	SPEED=2
	SPAWN=2 #SPAWN is the number of new asteroids that an asteroid spawns when it’s destroyed
	POINTS = 30 #The constant will act as a base value for the number of points an asteroid is worth. The actual point value will be modified according to the size of the #asteroid—smaller asteroids will be worth more than larger ones
	total=0 # In order to change levels, the program needs to know when all of the asteroids on the current level are destroyed so keep track of the total number of asteroids with #a new class variable  'total'
	# Create a dictionary for images
	
	
	# Constructor of Asteroid should initialize x, y and size of asteroids
	def __init__(self,game, x,y,size):
		Asteroid.total += 1 # Increase total count of asteroids in a level
		"""Based on size, the correct image for the new asteroid is retrieved and then passed along to Sprite’s constructor (since
		Sprite is the superclass of Asteroid). The x and y values passed to Asteroid for the location of
		the new space rock are also passed on to Sprite’s constructor."""
		
		super(Asteroid,self).__init__(image=Asteroid.images[size],
									x=x,
									y=y,
									dx=random.choice([1,-1])*Asteroid.SPEED*random.random()/size, 
									#velocity calculated as (1 or 0 or -1*SPEED*random no/size) as velocity can be either 0,+ or -ive
									dy=random.choice([1,-1])*Asteroid.SPEED*random.random()/size)
		self.game=game # An asteroid should be able to send the Game object a message, so I give each Asteroid object a reference to the Game object. I accept the Game object in #the Asteroid constructor by creating a new parameter
		self.size=size # This is not in games.Sprite
		
	
	def die(self):
		Asteroid.total -= 1
		self.game.score.value += int(Asteroid.POINTS / self.size)
		self.game.score.right = games.screen.width - 10
		if self.size!=Asteroid.SMALL:
			for i in range(Asteroid.SPAWN):
				new_asteroid=Asteroid(game=self.game,x=self.x,
									  y=self.y,
									  size=self.size-1) # Large will be redeveloped in 2 medium sized asteroids and Medium will be in two small asteroids
				games.screen.add(new_asteroid)
				
		""" Toward the end of Asteroid’s die() method, I test Asteroid.total to see if all the asteroids have been destroyed. If so, the final asteroid invokes the Game object’s 	advance() method, which advances the game to the next level and creates a new group of asteroids."""
		if Asteroid.total == 0:
			self.game.advance()
		super(Asteroid,self).die() # if size is small, medium or large, destroy each but for large and medium astroids two new medium and small asteroids are created
		
	
class Ship(Collider):
	# Load the ship's Image and thrust sound file 
	image = games.load_image("ship.bmp")
	sound = games.load_sound("thrust.wav")
	ROTATION_STEP = 3
	VELOCITY_STEP=.03 # Higher Number makes ship accelerate faster and lower number makes it accelerate slower
	MISSILE_DELAY = 25 # represents the delay a player must wait between missile firings
	VELOCITY_MAX = 3
	# Constructor of the Ship
	def __init__(self,game, x, y):
		super(Ship,self).__init__(image=Ship.image,x=x, y=y)
		self.game=game
		self.missile_wait=0 # First time the ship will can fire missile without waiting but next time onwards it has a wait time=delay

	# Move the ship
	""" The player can press the up arrow key to engage the ship’s engine. This applies thrust to the ship in the direction the ship is facing. Since there’s no friction, the ship  keeps moving based on all of the thrust the player applies to it. 
	When the player engages the ship’s engine, the code  changes the velocity of the ship based on the ship’s angle (and produces an appropriate sound effect, too)"""

	def update(self):
		#print(self.missile_wait)
		super(Ship, self).update()
		""" Rotate based on keys pressed. """
		if games.keyboard.is_pressed(games.K_LEFT):
			self.angle -= Ship.ROTATION_STEP # Subtract 3 degrees
		if games.keyboard.is_pressed(games.K_RIGHT):
			self.angle += Ship.ROTATION_STEP # Add 3 degrees
		if games.keyboard.is_pressed(games.K_UP):
			Ship.sound.play()
			
			#when the player presses the up arrow key, we need to alter the ship’s velocity components(the Ship object’s dx and dy).
			# First convert degrees tro radians
			angle=self.angle*math.pi/180
			# Use sin=Perp/Hyp and cos=Base/Hyp
			self.dx+=Ship.VELOCITY_STEP * math.sin(angle) # x is horizontal so  use sin() to find dx(base); Ship's last position is retained to find out next position
			self.dy+=Ship.VELOCITY_STEP * -math. cos(angle) # y is perp so use cos() to find dy (perp)
			# cap velocity in each direction- I cap the ship’s speed to avoid several potential problems, including the ship running into its own missiles.
			self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
			self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
		if self.missile_wait>0:
			self.missile_wait-=1
		"""Firing Missiles- allows the player to fire missiles by pressing the spacebar, the code below limits the missile fire rate by creating a countdown that forces a delay between missile firings. Once the countdown ends, the player is able to fire another missile."""
		if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait==0:
			new_missile=Missile(self.x, self.y, self.angle) # New Missile will have a x and y and an angle to be given to its constructor to calculate velocity  etc.
			games.screen.add(new_missile)
			self.missile_wait=Ship.MISSILE_DELAY

			
	def die(self):
		""" Destroy ship and end the game. """
		self.game.end()
		super(Ship, self).die()
		
			
class Missile(Collider):
	# Load the image and sound file
	image=games.load_image("missile.bmp")
	sound=games.load_sound("missile.wav")
	BUFFER=40  # Missile should have a constant buffer(distance from the ship that a new missile is created (so that the missile isn’t created on top of the ship)
	VEOCITY_FACTOR=7 # VELOCITY_FACTOR affects how fast the missile travels
	LIFETIME=40 # LIFETIME represents how long the missile exists before it disappears (so that a missile won’t float around the screen forever)
	
	
	def __init__(self,ship_x,ship_y,ship_angle): # Everytime a missile gets created pass on the ship's  positionn to find out where would be the missile
		Missile.sound.play() # Play the sound as soon as a missile gets created
		"""Where the missile is created depends upon where the ship is located, and how the missile travels depends upon the angle of the ship"""
		angle=ship_angle*math.pi/180 # angle is in radians
		buffer_x=Missile.BUFFER * math.sin(angle)
		buffer_y=Missile.BUFFER * math.cos(angle)
		x=ship_x+buffer_x 
		y=ship_y+buffer_y
		
		# Calculate velocity of missile
		dx=Missile.VEOCITY_FACTOR * math. sin(angle)
		dy=Missile.VEOCITY_FACTOR * -math.cos(angle)
		
		super(Missile,self).__init__(image=Missile.image, # class variable needs class name
									x=x,y=y, # function variable in the same func do not need class name
									dx=dx,dy=dy)
		self.lifetime=Missile.LIFETIME
		
	# Method for movement of missile
	def update(self):
		super(Missile, self).update()
		# If the missile's lifetime finishes then destroy the missile
		self.lifetime-=1 # decrease the count of lifetime
		if self.lifetime==0:
			self.destroy()

class Explosion(games.Animation):
	""" Explosion animation. """
	sound = games.load_sound("explosion.wav")
	images = ["explosion1.bmp",
			  "explosion2.bmp",
			  "explosion3.bmp",
			  "explosion4.bmp",
			  "explosion5.bmp",
			  "explosion6.bmp",
			  "explosion7.bmp",
			  "explosion8.bmp", 
			  "explosion9.bmp"]
	def __init__(self, x, y):
		super(Explosion, self).__init__(images = Explosion.images,
										x = x, 
										y = y,
										repeat_interval = 4, 
										n_repeats = 1,
										is_collideable = False) 
		# I pass is_collideable the value False so that the explosion animation doesn’t count as a collision for other sprites that might happen to overlap it.
		Explosion.sound.play()
	
class Game(object): #The Game itself could certainly be an object with methods like play() to start the game, advance() to move the game to the next level, and end() to end the game.
	""" The game itself. """
	def __init__(self):
		""" Initialize Game object.
		level is an attribute for the current game level number. sound is an attribute for the leveladvance sound effect. score is an attribute for the game score—it’s a Text object that appears in the upper-right corner of the screen. The object’s is_collideable property is False, which means that the score won’t register in any collisions—so the player’s ship won’t “crash into” the score and explode! Finally, ship is an attribute for the player’s ship."""
		
		# set level
		self.level = 0
		
		# load sound for level advance
		self.sound = games.load_sound("level.wav")
		
		# create score
		self.score = games.Text(value = 0,
								size = 30,
								color = color.white,
								top = 5,
								right = games.screen.width - 10,
								is_collideable = False)
		games.screen.add(self.score)
		
		# create player's ship
		self.ship = Ship(game = self,
						 x = games.screen.width/2,
		                 y = games.screen.height/2)
		games.screen.add(self.ship)
		
	def play(self):
		""" Play the game. """
		
		# begin theme music
		games.music.load("theme.mid")
		games.music.play(-1) # -1 : Forever
		
		# load and set background
		nebula_image = games.load_image("nebula.jpg")
		games.screen.background = nebula_image
		
		# advance to level 1
		self.advance()
		
		# start play
		games.screen.mainloop()
	def advance(self):
		""" Advance to the next game level. """
		self.level += 1	
		"""Creating the new wave of asteroids. Each level starts with the number of asteroids equal to the level number. So, the first level starts with only one asteroid, the second with two, and so on. Now, creating a bunch of asteroids is easy, but I need to make sure that no new asteroid is created right on top of the ship. Otherwise, the ship will explode just as the new level begins."""
		# amount of space around ship to preserve when creating asteroids
		BUFFER = 150 #BUFFER is a constant for the amount of safe space needed around the ship. BUFFER=x_min+y_min
		# create new asteroids
		for i in range(self.level):
			# calculate an x and y at least BUFFER distance from the ship
			# choose minimum distance along x-axis and y-axis
			x_min = random.randrange(BUFFER)# x_min is the minimum distance the new asteroid should be from the ship along the x-axis,
			y_min = BUFFER - x_min # y_min is the minimum distance that the new asteroid should be from the ship alongthe y-axis
			# choose distance along x-axis and y-axis based on minimum distance
			x_distance = random.randrange(x_min, games.screen.width - x_min) # x_distance is the distance from the ship for the new asteroid along the x-axis, It is a randomly
			#selected number that ensures that the new asteroid will be at least x_min distance from the ship
			y_distance = random.randrange(y_min, games.screen.height - y_min) # y_distance is the distance from the ship for the new asteroid along the y-axis. It is a randomly #selected number that ensures that the new asteroid will be at least y_min distance from the ship
			# calculate location based on distance
			x = self.ship.x + x_distance #x is the x-coordinate for the new asteroid
			y = self.ship.y + y_distance #y is the y-coordinate for the new asteroid
			# wrap around screen, if necessary
			x %= games.screen.width
			y %= games.screen.height
			# create the asteroid
			new_asteroid = Asteroid(game = self,x = x, y = y,size = Asteroid.LARGE)
			games.screen.add(new_asteroid)
			# display level number
		level_message = games.Message(value = "Level " + str(self.level),
										  size = 40, 
										  color = color.yellow,
										  x = games.screen.width/2,
										  y = games.screen.width/10,
										  lifetime = 3 * games.screen.fps,
										  is_collideable = False)
		games.screen.add(level_message)
			
			# play new level sound (except at first level)
		if self.level > 1:
			self.sound.play()
			
	def end(self):
		""" End the game. """
		# show 'Game Over' for 5 seconds
		end_message = games.Message(value = "Game Over",
									size = 90,
									color = color.red,
									x = games.screen.width/2,
									y = games.screen.height/2,
									lifetime = 5 * games.screen.fps,
									after_death = games.screen.quit,
									is_collideable = False)
		games.screen.add(end_message)
		
		
		
		
		
def main():
	astrocrash = Game()
	astrocrash.play()
	

main()
	
		
	
	






	
	
	
	

	
