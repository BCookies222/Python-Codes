# Longevity : Secret to lIve a  Long Life

from Tkinter import *

class Application(Frame): # Frame is Super Class of Application
	def __init__(self, master): # CONSTRUCTOR
		Frame.__init__(self, master) # master =root (Window)
		self.grid()
		self.ans=""
		self.create_widgets()
		
	def create_widgets(self):
		# Creating Labels for Heading and Password
		self.L=Label(self,text="Enter the password for the secret of Longevity")
		self.L.grid(row=0,column=0,columnspan=2,sticky=W)
		self.P=Label(self, text="Password")
		self.P.grid(row=1,column=0,sticky=W)
		
		# Create an Entry widget: User input , SINGLE LINE ENTRY
		self.E=Entry(self)
		self.E.grid(row=1,column=1, sticky=W)
		
		# Create a Button Widget" SUBMIT and attach it to the event handler
		self.B=Button(self,text="SUBMIT", command=self.reveal)
		self.B.grid(row=2,column=0,sticky=W)
		
		# Create a Text (space) widget to write multilines into
		self.T=Text(self,width=60, height=5,wrap=WORD)
		self.T.grid(row=3,column=0, columnspan=2,sticky=W)
		
	# Event Handler	
	def reveal(self):
		ans=self.E.get()
		if ans=="secret" or ans=="Secret":	
			message="Here's the secret to live long! Live to 99 then be very careful!"
			
		else:
			message="Incorrect Password"
			
		# Delete old text and insert new text
		self.T.delete(0.0,END) # Delete previously held text in T
		self.T.insert(0.20,message)	# Insert New Text
	
		
		
# main 
root=Tk()
root.title("Longevity")
root.geometry("500x300")
app=Application(root)
root.mainloop()