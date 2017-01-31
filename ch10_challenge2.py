# Write a version of the Guess My Number Game from chapter3 project using GUI

from Tkinter import *
import random
import time

class Application(Frame):
	def __init__(self,master):
		# Initilaize the Frame and also this Application
		Frame.__init__(self,master)
		self.grid()
		self.no_tries=0  # number of tries
		self.create_widgets()
		
		
	def create_widgets(self):
		# Create a Label widget"
		self.number=random.randint(1,20)
		print self.number
		Label(self,text="I'm thinking of a number between 1 and 20.").grid(row=0, column=0, columnspan=2, sticky=W)
		Label(self, text="Try to guess it in as few attempts as possible.").grid(row=1, column=0, columnspan=2, sticky=W)
		Label(self, text="Take a guess.").grid(row=2, column=0, sticky=W)
		self.g1=Entry(self)
		self.g1.grid(row=2, column=1, sticky=W)
		self.g1.insert(0,"")
		self.no_tries=0
		self.success = False
		if (self.no_tries==1 or self.no_tries==2 or self.no_tries==0) and (self.success==False):
			self.f=False
			Button(self, text="Check",command=self.reveal).grid(row=3, column=0, sticky=W)
		
		
		Button(self, text="Exit",command=self.exiting).grid(row=4,column=0, sticky=W)
	
		self.t=Text(self,width=40, height=10, wrap=WORD)
		self.t.grid(row=5,column=0, sticky=W)
		self.t.delete(0.0,END)
		
		
	def reveal(self):
		
		ans=""
		g=self.g1.get() # Important to convert entry of the entry widget from str to int
		guess=int(g)
			
		if (self.number==guess) and self.f==False:
			self.success=True
			self.f	=True
			ans+="Yes, You guessed it and it only took you "+str(self.no_tries+1)+" try/tries"
			ans+="\n"+"You may exit now"
			self.g1.delete(0,'end')	
			
			
		if self.number!=guess:
			if (self.number < guess):	
					ans+="Try Again!"+"\n"+"HINT: Lower..."
					self.f=False
					self.no_tries+=1
					
			if (self.number>guess):
					ans+="Try Again!"+"\n"+"HINT: Higher..."
					self.f=False
					self.no_tries+=1
				#self.g1.delete(0,'end')
		
		if (self.no_tries>2)and self.number!=guess:
			self.success=True
			self.g1.delete(0,'end')	
			ans="Sorry! You have tried maximum amount of times"+"\n"+"The number is="+str(self.number)+"\n"+"You must exit now"
			self.g1.delete(0,'end')
			self.f=True

		self.number=int(self.number)
		self.g1.delete(0,'end')	
			
		self.t.delete(0.0,END)
		self.t.insert(0.0,ans)
	def exiting(self):
		exit(0)
		
		

		self.t.delete(0.0,END)
		self.t.insert(0.0,ans)
		
		
			
			


# mainloop

root=Tk()
root.title("Guess My Number")
root.geometry("300x200")
app=Application(root)
root.mainloop()