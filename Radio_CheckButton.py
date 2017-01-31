# Createcheck buttons for ype of Movies from a List and Radio Buttons for Language

from Tkinter import *

class Application(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
		
		
	def create_widgets(self):
		# Create Labels
		Label(self, text="Choose your favorite movie").grid(row=0, column=0,sticky=W)
		Label(self, text="Select all that apply:").grid(row=1, column=0,sticky=W)
	
		# Create Check Button Widgets
		self.likes_comedy=BooleanVar() # Object of class BooleanVar for  comedy check button 
		Checkbutton(self,text="Comedy",variable=self.likes_comedy,command=self.update_text).grid(row=2, column=0, sticky=W)
	
		self.likes_drama=BooleanVar()# Object of class BooleanVar for  drama check button 
		Checkbutton(self,text="Drama",variable=self.likes_drama,command=self.update_text).grid(row=3, column=0, sticky=W)
	
		self.likes_romantic=BooleanVar() # Object of class BooleanVar for  romantic check button 
		Checkbutton(self,text="Romantic",variable=self.likes_romantic,command=self.update_text).grid(row=4, column=0, sticky=W)
	
		# Create Radio Button Widget 
		self.language=StringVar()
		Radiobutton(self, text="English",variable=self.language,value="English.",command=self.update_text).grid(row=5,column=0, sticky=W)
		Radiobutton(self, text="Hindi",variable=self.language,value="Hindi.",command=self.update_text).grid(row=6,column=0, sticky=W)
		
		# Create a Text Widget-Dimensions need to be given
		self.T=Text(self,width=40, height=4, wrap=WORD)
		self.T.grid(row=7,column=0, columnspan=3)
	
	def update_text(self):
		cb_ans=""
		rb_ans=""
		
		if self.likes_comedy.get(): # Selected Comedy
			cb_ans+="You like Comedy Movies!"+"\n"
		if self.likes_drama.get(): # Selected Comedy
			cb_ans+="You like Drama Movies!"+"\n"
		if self.likes_romantic.get(): # Selected Comedy
			cb_ans+="You like Romantic Movies!"+"\n"	
		rb_ans+="The movie(s) will be played in "+self.language.get()	
			
		self.T.delete(0.0,END)
		self.T.insert(0.0,cb_ans+rb_ans)


# Main 

root=Tk()
root.title("Movie Chooser")
root.geometry("300x200")
app=Application(root)
root.mainloop()
