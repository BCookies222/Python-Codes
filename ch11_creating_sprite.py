# Creating a sprite

from livewires import games, color

games.init(screen_width=1000, screen_height=500, fps=50) # creating screen

# Load Image 
wall_image=games.load_image("Wall.jpg",transparent=False) # Upload the image to a variable. 

# Assign it to background of screen
games.screen.background=wall_image # assign the variable to the background property of screenn object

# Create Texts
Wel_text=games.Text(value="WELCOME TO BRICK WALL", size=30, x=500, y=10,color=color.green)
fees=games.Text(value="Entry Fees",size=25, x=130, y=30, color=color.red)
adults_fees=games.Text(value="Fees for Adults(Age:13 and 59): Rs.1000",size=20, x=135, y=60, color=color.red)
child_fees=games.Text(value="Fees for Children(Age:0-12years): Rs.300",size=20, x=138, y=100, color=color.red)
senior_fees=games.Text(value="Fees for Seniors(Age:60and above): Rs.150",size=20, x=145, y=140, color=color.red)

# Add Text to screen
games.screen.add(Wel_text)
games.screen.add(fees)
games.screen.add(adults_fees)
games.screen.add(child_fees)
games.screen.add(senior_fees)

# Laod an image for Sprite- Moving Object

adults=games.load_image("adults.jpg", transparent=False)
child=games.load_image("child.jpg", transparent=False)
seniors=games.load_image("seniors.jpg", transparent=False)

# Create Sprite with loaded image
a=games.Sprite(image=adults,x=350,y=60)
c=games.Sprite(image=child,x=350,y=100)
s=games.Sprite(image=seniors,x=350,y=140)

# Add the Sprite objects to screen
games.screen.add(a)
games.screen.add(c)
games.screen.add(s)

# Create a Message-A message is a text with a lifetime
m=games.Message(value="Things to do",size=20, color=color.pink,x=500,y=180,lifetime=100,after_death=games.screen.quit) # 250 mainloop cycles

# Add message to games
games.screen.add(m)

games.screen.mainloop()




