# Create a Screen: FROM HERE ON USING Pyhton 3.1 Earlier Codes Chapter 1-10 are using Python2.7

from livewires import games,color # livewires  is a pygame wrapper and games is a module

SCREEN_WIDTH=680
SCREEN_HEIGHT=480

games.init(SCREEN_WIDTH,SCREEN_HEIGHT,fps=50)# games is a module and init is for initialization of screen

wall_image=games.load_image("Ooty-Rose-Garden.jpg", transparent=False) # load_image is a method of games module
games.screen.background=wall_image # screen is the object of games module and background is the property of screen

text=games.Text(value="WELCOME TO OOTY",x=340,y=30,size=30,color=color.pink)
games.screen.add(text) # add is a method of screen object

games.screen.mainloop()

