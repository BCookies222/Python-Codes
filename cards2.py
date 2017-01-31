""" This is cards module for chapter 9 challenge 2"""


class Card(object): # This is class Card
	"""A Playing Card"""
	RANKS=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
	SUITS=["c","d","h","s"]
	def __init__(self,rank,suit, face_up=True): # Constructor
		self.rank=rank
		self.suit=suit
		self.is_face_up=face_up
		
	def __str__(self): # Object Representation
		if self.is_face_up:
			rep=self.rank+self.suit
		else:
			rep="XX"
		return rep
		
	def flip(self):
		if self.is_face_up:
			self.is_face_up=not self.is_face_up
		

class Hand(object):
	"A Hand of playing cards"
	def __init__(self): # Constructor
		self.cards=[] # cards is a LIST
		
		
	def __str__(self): # Object Representation
		if self.cards:
			rep=""
			for card in self.cards: # card is one element of LIST cards
				rep=rep+str(card)+"\t"
		else:
			rep="<empty>"
		return rep
	def clear(self):
		self.cards=[]
		
	def add(self, card):
		self.cards.append(card)
		
	def give(self,card,other_hand):
		self.cards.remove(card)
		other_hand.add(card)
		
class Deck(Hand): # Hand is the Base class of Deck(derived class). Because a Deck is a specialized hand that can do everything a Hand can but can also do : populate, shuffle, deal cards to hands
	"""A deck of playing cards"""
	def populate(self):
		for suit in Card.SUITS: # if the attribute is not a part of this class or derived then use the class name <dot> attribute name
			for rank in Card.RANKS:
				self.add(Card(rank,suit)) # Card(rank,suit) is the object of class Card,that is passed to add() of class Hand. Hand is the Base class of Deck. This is e.g of combining objects.
				#i.e this is two objects communicating. Here the messsage is being received by the add() of class Hand. Self is the object of class Deck
				
	def shuffle(self):
		import random
		random.shuffle(self.cards) # Calling inbuilt shuffle() of module random
		
	def deal(self,hands,per_hand=1):
		# Error Checking
		L=len(hands) # No. of players
		q=len(self.cards)-L*per_hand # 52-no.of players * per_hand
		print"Deck has",q," cards left after the following move"
		if q>L:
			
			for rounds in range(1): # starts from 0 to per_hand-1
				for hand in hands:
					if self.cards:
						top_card=self.cards[0]
						self.give(top_card,hand)
		elif(q<=L):
			print " Repopultaing and reshuffling"
			self.populate()
			self.shuffle()	
		

if __name__=="__main__":
	print"You ran this module directly and did not import it"
	input("Press Enter to exit")
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
			
				
		
		
		
		
