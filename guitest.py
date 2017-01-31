from Tkinter import * # Module Tkinter

root=Tk() # Create a Object of class Tkinter

root.title("Welcome to Delhi Delights")
root.geometry("1200x100")
app=Frame(root) # Add Frame to window named object(root)
app.grid() # To show the Frame in side the window
lb1=Label(app,text="Break Fast Menu")
lb1.grid() # To show the Label in the frame

# Create a Button (in three ways that does NOTHING as of now) inside Frame
bt1=Button(app, text="Tea and Cookies")
bt1.grid()
bt2=Button(app)
bt2.grid()
bt2.configure(text="Toast and Coffee!") # assigning the text for the button at a later stage

bt3=Button(app)
bt3.grid()
bt3["text"]="From the oven"

root.mainloop()
