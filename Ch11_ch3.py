#Create a simple one player game of pong where a player controls the paddle and the ball bounces of three walls. If the ball gets by the player's paddle the game is over.

from livewires import games, color
import random

games.init(screen_width=640, screen_height=480, fps=100)

class Paddle(games.Sprite):
	paddle_pic=games.load_image("paddle.PNG")
	def __init__(self): #Paddle will have image and x and y coordinates
		super(Paddle,self).__init__(image=Paddle.paddle_pic, 
									x=games.mouse.x,
									bottom=games.screen.height)
	# If score was in the init() then its an instance variable	
	score=games.Text(value=0, size=50, color=color.green,top=10, x=games.screen.width-10)  # Not a instance variable but a class variable
	games.screen.add(score)
		
	def update(self):
		self.x=games.mouse.x
		if self.left<0: 
			self.left=0
		if self.right>games.screen.width:
			self.right=games.screen.width
			
		self.check_catch()	
		
	def check_catch(self):
		for b in self.overlapping_sprites:
			self.score.value+=10 # Add 10 to score?? The score keeps increasing  ************ Very Important need to know WHY
			self.score.right=games.screen.width-10 # Move the score from right edge 10 pixels away
			b.handle_caught()
	def destruction(self):
		#self.destroy()
		games.mouse.is_visible=True
  
			
class Pong(games.Sprite):
	pong_pic=games.load_image("Pong.JPG")
	pong_speed=1
	
	def __init__(self,x_pong=games.screen.width/3,y=15):
	
		super(Pong,self).__init__(image=Pong.pong_pic,
								  x=x_pong,
								  y=y,
								  dy=Pong.pong_speed)
				
	def update(self):
		if self.bottom > games.screen.height:
			#Paddle.score.value+=0
			#for a in self.overlapping_sprites: # Pong's overlapping is PADDLE so destroy paddle
				#a.destruction()
			self.end_game()
			self.destroy()
	
	def handle_caught(self):
		self.destroy()
		
	def end_game(self):
		Mesg=games.Message(value="Game Over!", size=50, color=color.brown,
						   x=games.screen.width/2,
						   y=games.screen.height/2,
						   lifetime=1*games.screen.fps,
						   after_death=games.screen.quit)
						   
		games.screen.add(Mesg)
class Hand(games.Sprite):
	
	image = games.load_image("chef.jpg")
	def __init__(self, y =10, speed = 2, odds_change = 200):
		""" Initialize the Chef object. """
		super(Hand, self).__init__(image =Hand.image,x = games.screen.width/2,y = y,dx = speed)
		self.odds_change = odds_change
		self.time_til_drop = 0
	def update(self):
		if self.left < 0 or self.right > games.screen.width:
			self.dx = -self.dx
		elif random.randrange(self.odds_change) == 0:
			self.dx = -self.dx
		self.check_drop()
	def check_drop(self):
		""" Decrease countdown or drop pizza and reset countdown. """
		if self.time_til_drop > 0:
			self.time_til_drop -= 1
		else:
			new_pong = Pong(x_pong=self.x)
			games.screen.add(new_pong)
			# set buffer to approx 30% of pizza height, regardless of pizza speed   
			self.time_til_drop = int(new_pong.height*1.3 /Pong.pong_speed) + 1

 
def main():
	
	wall_pic=games.load_image("Wall.jpg", transparent=False)
	games.screen.background=wall_pic
	
	the_paddle=Paddle()
	games.screen.add(the_paddle)
	
	the_pong=Pong()
	games.screen.add(the_pong)
	
	the_hand=Hand()
	games.screen.add(the_hand)
	
	games.mouse.is_visible=False
	games.mouse.event_grab=True
	
	games.screen.mainloop()
	print(the_paddle.score.value)
	
main()
		
	
			
		
			
			
			
		
	


#Create a simple one player game of pong where a player controls the paddle and the ball bounces of three walls. If the ball gets by the player's paddle the game is over.

from livewires import games, color
import random

games.init(screen_width=640, screen_height=480, fps=50)

class Paddle(games.Sprite):
	paddle_pic=games.load_image("paddle.PNG")
	def __init__(self): #Paddle will have image and x and y coordinates
		super(Paddle,self).__init__(image=Paddle.paddle_pic, 
									x=games.mouse.x,
									bottom=games.screen.height)
	# If score was in the init() then its an instance variable	
	score=games.Text(value=0, size=50, color=color.green,top=10, x=games.screen.width-10)  # Not a instance variable but a class variable
	games.screen.add(score)
		
	def update(self):
		self.x=games.mouse.x
		if self.left<0: 
			self.left=0
		if self.right>games.screen.width:
			self.right=games.screen.width
			
		self.check_catch()	
		
	def check_catch(self):
		for b in self.overlapping_sprites:
			self.score.value+=10 # Add 10 to score?? The score keeps increasing  ************ Very Important need to know WHY
			self.score.right=games.screen.width-10 # Move the score from right edge 10 pixels away
			b.handle_caught()
	def destruction(self):
		#self.destroy()
		games.mouse.is_visible=True
  
			
class Pong(games.Sprite):
	pong_pic=games.load_image("Pong.JPG")
	pong_speed=1
	
	def __init__(self,x_pong=games.screen.width/3,y=10):
	
		super(Pong,self).__init__(image=Pong.pong_pic,
								  x=x_pong,
								  y=y,
								  dy=Pong.pong_speed)
				
	def update(self):
		if self.bottom > games.screen.height:
			Paddle.score.value+=0
			for a in self.overlapping_sprites: # Pong's overlapping is PADDLE so destroy paddle
				a.destruction()
			self.end_game()
			self.destroy()
	
	def handle_caught(self):
		self.destroy()
		
	def end_game(self):
		Mesg=games.Message(value="Game Over!", size=50, color=color.brown,
						   x=games.screen.width/2,
						   y=games.screen.height/2,
						   lifetime=1*games.screen.fps,
						   after_death=games.screen.quit)
						   
		games.screen.add(Mesg)
class Hand(games.Sprite):
	
	image = games.load_image("ball_hand.jpg")
	def __init__(self, y =5, speed = 2, odds_change = 200):
		""" Initialize the Chef object. """
		super(Hand, self).__init__(image =Hand.image,x = games.screen.width/2,y = y,dx = speed)
		self.odds_change = odds_change
		self.time_til_drop = 0
	def update(self):
		if self.left < 0 or self.right > games.screen.width:
			self.dx = -self.dx
		elif random.randrange(self.odds_change) == 0:
			self.dx = -self.dx
		self.check_drop()
	def check_drop(self):
		""" Decrease countdown or drop pizza and reset countdown. """
		if self.time_til_drop > 0:
			self.time_til_drop -= 1
		else:
			new_pong = Pong(x_pong=self.x)
			games.screen.add(new_pong)
			# set buffer to approx 30% of pizza height, regardless of pizza speed   
			self.time_til_drop = int(new_pong.height*1.3 /Pong.pong_speed) + 1

 
def main():
	
	wall_pic=games.load_image("Wall.jpg", transparent=False)
	games.screen.background=wall_pic
	
	the_paddle=Paddle()
	games.screen.add(the_paddle)
	
	the_pong=Pong()
	games.screen.add(the_pong)
	
	the_hand=Hand()
	games.screen.add(the_hand)
	
	games.mouse.is_visible=False
	games.mouse.event_grab=True
	
	games.screen.mainloop()
	print(the_paddle.score.value)
	
main()
		
	
			
		
			
			
			
		
	


