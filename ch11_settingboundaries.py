# Setting the bundaries

from livewires import games,color

# Create a class

class Mypizza(games.Sprite): # c in class is in lower case. Mypizza is inheriting from super class:Sprite
	# Use the Sprite's update method-By default it does nothing but we will tailor it according to our needs
	def update(self):
		if self.right>games.screen.width or self.left<0:
			self.dx=-self.dx
		if self.bottom>games.screen.height or self.top<0:
			self.dy=-self.dy
			

def main():
	# Global Variables
	
	# set the screen
	games.init(screen_width=640, screen_height=480,fps=50)

	# Upload the image
	wall_pic=games.load_image("Wall.jpg", transparent=False)

	# set the uploaded image to background of screen
	games.screen.background=wall_pic
	
	#Create a score
	score=games.Text(value="Score:173847",color=color.brown,size=60,x=550,y=30)
	# Create a Message
	msg=games.Message(value="You Won!",color=color.pink,size=30,x=games.screen.width/2,y=games.screen.height/2,lifetime=1500,after_death=games.screen.quit)
	# upload the pic of Sprite-Pizza
	piz_img=games.load_image("pizza.jpg")
	pizza_pic=Mypizza(image=piz_img,x=games.screen.width/2, y=games.screen.height/2, dx=1, dy=1)
	games.screen.add(score)
	games.screen.add(pizza_pic)
	games.screen.add(msg)
	games.screen.mainloop()
	
	
main()
		


