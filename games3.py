"""This is games module for challenge 3 of chapter 9"""



class Player(object):
	""" A player for a game"""
	def __init__(self,name,score=0):	# Constructor
		self.name=name
		self.score=score
	def __str__(self):	# Object Representation
		rep=self.name+":\t"+str(self.score)
		return rep
def ask_yes_no(question):
	"""Ask a yes or no question"""
	response=None
	while response not in ("y","n"):
		response=raw_input(question).lower()
	return response
	
def ask_number(question,low,high):
		"""Ask a number within a range"""
		response=None
		while response not in range(low,high):
			response=int(raw_input(question))
		return response

if __name__=="__main__":
	print"You ran this module directly and did not import it"
	input("Press Enter to exit")
			
			
			
			
			
			
			