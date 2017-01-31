#The Madlib program
from Tkinter import *

class Application(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()
		
		
	
	def create_widgets(self):
		Label(self,text="Enter Informaton for a new story").grid(row=0,column=0,columnspan=2,sticky=W) # This is a big text so give it columnspans
		Label(self,text="Person:").grid(row=1,column=0,sticky=W)
		Label(self,text="Plural Noun:").grid(row=2,column=0,sticky=W)
		Label(self,text="Verb:").grid(row=3,column=0,sticky=W)
		Label(self,text="Adjective(s):").grid(row=4,column=0,sticky=W)
		Label(self,text="Body Part:").grid(row=5,column=0,sticky=W)  # Belly Button, Big Toe, Medulla Oblongata
		
		# Single Line Entries Widgets
		self.E1=Entry(self) # Person
		self.E1.grid(row=1, column=1, sticky=W)
		self.E2=Entry(self) # Plural Noun
		self.E2.grid(row=2, column=1, sticky=W)
		self.E3=Entry(self) # Verb
		self.E3.grid(row=3, column=1, sticky=W)
		
		
		# Create check Button for Adjectives
		self.itchy=BooleanVar()
		Checkbutton(self,text="Itchy",variable=self.itchy).grid(row=4, column=1, sticky=W)
		self.joyous=BooleanVar()
		Checkbutton(self,text="Joyous",variable=self.joyous).grid(row=4, column=2, sticky=W)
		self.electric=BooleanVar()
		Checkbutton(self,text="Electric",variable=self.electric).grid(row=4, column=3, sticky=W)
		
		
		# Create Radio Button
		self.bp=StringVar() # one variable for all Radio Buttons
		
		Radiobutton(self, text="Belly Button", variable=self.bp, value="belly button").grid(row=5, column=1,sticky=W)
		# Text is the word shown as radio button but value is the string inserted if you choose that as the choice
		Radiobutton(self, text="Big Toe", variable=self.bp, value="big toe").grid(row=5, column=2,sticky=W)
		Radiobutton(self, text="Medula Oblongata", variable=self.bp,value="medula oblongata").grid(row=5, column=3,sticky=W)
		
		#Create a Button to click
		Button(self,text="Click for Story",command = self.tell_story).grid(row=6,column=0,sticky=W)
		
		# Create a Text widget to that can hold multilines _ TEXT Widgets always have width, height, wrap
		self.t=Text(self,width=75,height=10, wrap=WORD)
		self.t.grid(row=7,column=0, columnspan=4, sticky=W)
		
	
	def tell_story(self): 
		# Get user inputs for three Entry Boxes
		person=self.E1.get()
		plural_noun=self.E2.get()
		verb=self.E3.get()
			
		# See which Check Button was selected and you now more than 1 can be selected so you put a comma
		adj=""
		if self.itchy.get(): # If this option is selected
			adj+="itchy,"
		if self.joyous.get():
			adj+="joyous,"
		if self.electric.get():
			adj+="electric,"
				
		# See which Radio Button gets selected	
			
		body_part=self.bp.get()
		story=""
		story="The famous expolorer "
		story+=person
		story+=" had nearly given up a life long quest to find The Lost City of "
		story+=plural_noun
		story+=" when one day the "
		story+=plural_noun
		story+=" found "
		story+=person
		story+=" . A strong "
		story+=adj
		story+=" peculiar feeling overwhelmed the explorer. "
		story+="After all this time the quest was finally over. A tear came to "
		story+=person+"'s "
		story+=body_part+" ."
		story+=" And then,the "
		story+=plural_noun
		story+=" promptly devoured "
		story+=person
		story+=" . The moral of the story? Be careful what you "
		story+=verb
		story+=" for."
		
		
		self.t.delete(0.0,END)
		self.t.insert(0.0,story)
			





# Main Loop
root=Tk()
root.title("MadLib")
root.geometry("400x200")
app=Application(root)
root.mainloop()


