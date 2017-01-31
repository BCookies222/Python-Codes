# Pizza Game

from livewires import games, color

# Create a screen
games.init(screen_width=640, screen_height=480,fps=50)

# Upload a wall Image

wall_img=games.load_image("Wall.jpg",transparent=False)
games.screen.background=wall_img


#Create a score
score=games.Text(value="Score:173847",color=color.black,size=60,x=550,y=30)
#Add a score
games.screen.add(score)

# Create a Message
m=games.Message(value="YOU WON!",
				size=100,
				color=color.red, 
				x=games.screen.width/2, # width and height are properties of screen object
				y=games.screen.height/2, 
				lifetime=250, # Default valus is 0 i.e Never Destroy
				after_death=games.screen.quit)# () after quit not needed and Default Value is None

				
games.screen.add(m) # Message is a sub-class of Text so it inherits all properties of Text

# Create a pizza image and upload it
pizza_image=games.load_image("pizza.jpg",transparent=True)
#Use Sprite to create Pizza variable
pizza=games.Sprite(image=pizza_image,x=200,y=140,dx=1, dy=1)
# Sprite has image, x and y variables and to move give the dx and dy (velocity) values. Default value of dx and dy is 0
# +dx = right ; -dx means left, +dy=down and -dy=up
# dx=1 and dy=1 means everytime the graphics window is updated by mainloop the pizzas x-coordinate is increased by 1 and y coordinate is increased by 1
# moving the Sprite right and down
games.screen.add(pizza)



games.screen.mainloop()