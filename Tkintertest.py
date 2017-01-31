# Creating a window with a Frame that frame will have label and create 3 buttons using class

from Tkinter import *

class Application(Frame): # A GUI application for three Buttons. Class Application is invoked from Frame class of Tkinter module
	def __init__(self,master): # root is the master
		Frame.__init__(self, master) # Invoke the constructor of in built class"Frame" of module Tkinter. root(WIndow) is master
		self.grid() # Show the Frame
		self.create_widgets() # Call the create_widgets function 
		
		

	# Create Three Buttons
	def create_widgets(self):
		self.bt1=Button(self,text="I do nothing")
		self.bt1.grid()
		
		self.bt2=Button(self)
		self.bt2.grid()
		self.bt2.configure(text="Me too!")
		
		self.bt3=Button(self)
		self.bt3.grid()
		self.bt3["text"]="Same Here"
		
		
	
# main 	
root=Tk() # root is the Name of the object for the Tk class
root.title("Delhi Delights") # Use title for WINDOW and label that has text for Frames and Buttons
root.geometry("350x100")	
app=Application(root) # root is a WINDOW: object of class Tk and app is the object of Application class
root.mainloop() 