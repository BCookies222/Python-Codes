
""" The Game: Each Player tries to get total of 21 without going over. Numbered cards count as their face value. Ace can be 1 or 11(whichever is best for the player) and any
jack, queen or king count as 10.Computer is the dealer and it plays against the players. Cards are dealt to computer and all players. Players can see all of their cards and coputer
displays their total. However one of the computer's card is hidden.
Next, each players is allowed to additional cards. Each player can take one card at a time for as long as the player likes but if the total >21 (BUSTING), the player loses. If all
players bust then computer reveals its first card and the round is over.Otherwise the play continues. The computer must take additional cards as long as its total is <17.If the computer busts, all the players who have not busted, win. Otheriwse, each player's total is compared with computer's total. If the player's total is greater player wins otherwise loses and if their total are same the player ties with computer(Pushing)
"""

import cards,games

class BJ_Card(cards.Card): # cards : Module and Card is one of the classes of cards Module
	""" A BlackJack Card"""
	ACE_VALUE=1

	@property
	def value(self):
		if self.is_face_up:
			v=BJ_Card.RANKS.index(self.rank)+1 # for a card that has rank =6 , index=5 so +1 makes its value =6
			if v>10: # if rank is J,Q,K i.e indeces as 10,11,12 v=11,12,13 make that as V=10
				v=10
		else:
			v=None

		return v

class BJ_Deck(cards.Deck):# cards is a module and Deck is the class of that module
	""" A BlackJack deck"""
	def populate(self):
		for suit in BJ_Card.SUITS: # SUITS is attribute of class Card that is in module card. BJ_Card is a derived class of Card so automatically all attributes of class Card are also attributes of class BJ_Card
			for rank in BJ_Card.RANKS:
				self.cards.append(BJ_Card(rank,suit)) # BJ_Card(rank,suit) is Object of class BJ_Card
				# Here cards is attribute of Hand that is bse class of Deck which is the base class of BJ_Deck

class BJ_Hand(cards.Hand):
	""" A Black Jack Hand"""
	def __init__(self,name):
		super(BJ_Hand,self).__init__()# Use the constructor of its(BJ_Hand) super class i.e Hand's constructor
		self.name=name # new attribute=name

	def __str__(self):
		rep=self.name + ":\t"+super(BJ_Hand,self).__str__() # It prints name and represents card
		if self.total:
			rep=rep+"(" + str(self.total) + ")"
		return rep
	@property
	def total(self):
		for card in self.cards:  # If card in hand has a value of None then Total is None
			if not card.value: # since value is a property so value=v and to use that attribute (v) we just use property name
				return None

		# Add up each card values , treat each ACE as 1
		t=0
		for card in self.cards:
			t+=card.value
			
		
		# Determine if hand contains an ACE
		contains_ace=False # flag
		for card in self.cards:
			if card.value==BJ_Card.ACE_VALUE: # This is how classes communicate within a module i.e class name <dot> attribute name
				contains_ace=True

		#if hand contains_ace and total is low enough then treat Ace as 11:
		if contains_ace and t<=11:
			t+=10 # then add 10 as 1 was already added
			
		return t # total=t
	
	def is_busted(self):
		return self.total>21

class BJ_Player (BJ_Hand):
	""" A BlackJack Player"""
	def is_hitting(self): # Used games module
		response=games.ask_yes_no("\n"+self.name+", do you want a hit?(Y/N):  ")
		return response=="y"

	def bust(self):
		print(self.name,"busts")
		self.lose()

	def lose(self):
		print(self.name,"loses")

	def win(self):
		print(self.name,"wins")
	def push(self):
		print(self.name,"pushes")

class BJ_Dealer(BJ_Hand):
	"""  A BlackJack Dealer"""
	def is_hitting(self):
		return self.total<17

	def bust(self):
		print self.name,"busts"

	def flip_first_card(self):
		first_card=self.cards[0]
		first_card.flip()

class BJ_Game(object):
	def __init__(self,names):
		self.players=[]
		for name in names:
			player=BJ_Player(name)
			self.players.append(player)

		self.dealer=BJ_Dealer("Dealer")
		
		self.deck=BJ_Deck() # Object of BJ_Deck is assigned to deck
		self.deck.populate()
		self.deck.shuffle()
	@property
	def still_playing(self):
		sp=[]
		for player in self.players:
			if not player.is_busted():
				sp.append(player)
		return sp

	def __additional_cards(self,player):
		while not player.is_busted() and player.is_hitting():
			self.deck.deal([player])
			print(player)
			if player.is_busted():
				player.bust()


	def play(self):
		# Deal initial 2 cards to everyone
		self.deck.deal(self.players + [self.dealer],per_hand=2)
		self.dealer.flip_first_card()
		for player in self.players:
			print(player) # prints the card of players
		print(self.dealer) # prints the card of dealer
		

		for player in self.players:
			self.__additional_cards(player)
		self.dealer.flip_first_card()

		if not self.still_playing:
			# Since all players have busted just show the dealers hand
			print self.dealer

		else:
			# Deal additional cards to dealer
			print self.dealer
			self.__additional_cards(self.dealer)

			if self.dealer.is_busted():
				# everyone still playing wins
				for player in self.still_playing:
					player.win()

			else:
				# Compare each player still playing to dealer:
				for player in self.still_playing:
					#print"Player's Total", player.total
					#print"Dealer's Total",self.dealer.total
					if player.total>self.dealer.total:
						player.win()

					elif player.total<self.dealer.total:
						player.lose()
					else:
						player.push()

		for player in self.players:
			player.clear()
		self.dealer.clear()

def main():
	print"Welcome to Black Jack Game"
	names=[]
	number=games.ask_number("How Many Players?(1-7): ",low=1, high=8)
	print number
	for i in range(number):
		name=raw_input("Enter the player's Name: ")
		names.append(name)
	#print()
	game=BJ_Game(names) #game is the object of BJ_Game
	again=None
	while again!="n":
		game.play()
		again=games.ask_yes_no("Do you want to play again?: ")


main()
input("Press Enter to exit")







































