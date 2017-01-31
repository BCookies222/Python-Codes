# Count the number of click of a button

# Import Tkinter module

from Tkinter import *

class Application(Frame): # Inherit Application (to count no. of clicks of a button) from "Frame" Class
	# constructor
	def __init__(self, master): # self=app and master=root
		Frame.__init__(self, master) # invoke Frame's (super class of Application) constructor
		self.grid()
		self.count_clicks=0 # Initialize the variables 
		self.create_widgets() # Call  the function
		
	def create_widgets(self): # Button and a Label
		self.lb1=Label(self, text="Counting the number of clicks")
		self.lb1.grid()
		self.bt1=Button(self)
		self.bt1["text"]="Total clicks: 0" # First Message that Appears on screen
		self.bt1["command"]=self.update_count # This is a call to Event Handler. Although a method but DO NOT PUT () here while calling it
		self.bt1.grid()
		
	def update_count(self):
		self.count_clicks+=1
		self.bt1["text"]="Total Clicks: "+ str(self.count_clicks)
	



# Main part
root=Tk() # root: object of Tk class
root.title("Delhi Delights") # title and geometry are inbuilt funcs of Tk class and root is window
root.geometry("200x100")
app=Application(root) # root is passed as argument to the class Application's constructor so master=root
root.mainloop()
