""" Improve the BlackJack Project by allowing players to bet. Keep Track of each player's bankroll and remove any player who runs out of money"""
import cards3,games3
import random
from random import choice
import sys

class BJ_Card(cards3.Card): # cards : Module and Card is one of the classes of cards Module
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

class BJ_Deck(cards3.Deck):# cards is a module and Deck is the class of that module
	""" A BlackJack deck"""
	def populate(self):
		for suit in BJ_Card.SUITS: # SUITS is attribute of class Card that is in module card. BJ_Card is a derived class of Card so automatically all attributes of class Card are also attributes of class BJ_Card
			for rank in BJ_Card.RANKS:
				self.cards.append(BJ_Card(rank,suit)) # BJ_Card(rank,suit) is Object of class BJ_Card
				# Here cards is attribute of Hand that is bse class of Deck which is the base class of BJ_Deck

class BJ_Hand(cards3.Hand):
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
		# Add up each card values , treat each ACE as 1
		t = 0
		for card in self.cards:  # If card in hand has a value of None then Total is None
			if not card.value:  # since value is a property so value=v and to use that attribute (v) we just use property name
				t += 0
			else:
				t += card.value
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
		response=games3.ask_yes_no("\n"+self.name+", do you want a hit?(Y/N):  ")
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
		first_card.flip() # XX
		

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
			#print("Before player is dealt a card")
			self.deck.deal([player])
			#print("After the player is dealt a card")
			print(player)
			if player.is_busted():
				player.bust()


	def play(self):
		# Deal initial 2 cards to everyone
		
		#self.deck.deal(self.players + [self.dealer],per_hand=2)
		self.deack.run(self.player)
		#self.deck.deal([self.dealer],per_hand=)
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
	
	def run(self):
		
		
		money = 1000
		raw_input("Press <ENTER> To Begin")
		
		print "You have $",money,"in your bank."
		bet = raw_input("How much would you like to bet?")

		b=int(bet)

		cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
		# At a time two cards are drawn
		c1 = choice(cards)
		cards.remove(c1) 

		c2 = choice(cards)
		cards.remove(c2)

		psum = c1 + c2 # Player's sum of the cards

		print "You were dealt a",c1,"and a",c2,"for a sum of",psum,
		print "\n"
		hs = " " # Hit / Stand

		while psum < 21 and "s" not in hs:
			hs = raw_input("Hit or Stand (h or s): ").lower()
			if "h" in hs:
				c3 = choice(cards)
				cards.remove(c3)
				psum = psum + c3 # another card dealt
				print "You were dealt a",c3,"for a sum of",psum,
				print "\n"
			elif "s" in hs: # Standing
				print "Your final sum is",psum,

		print "\n"

		if psum > 21:
			print "Bust!" "\n" "You lose." "\n"
			money = money - b
			print "You now have $",money,"in your bank."
		elif psum == 21:
			print "You got a BlackJack!" "\n" "You win!" "\n"
			money = money + b
			print "You now have $",money,"in your bank."   
		else:
			print "Dealer's turn"

		if psum < 21:    # If psum<21 so dealer can play
			c4 = choice(cards)
			cards.remove(c4) 

			c5 = choice(cards)
			cards.remove(c5)

			dsum = c4 + c5 # Dealer's sum of cards

			while dsum < 17: # If dsum <17 then dealer dealt with another card
				c6 = choice(cards)
				cards.remove(c6)
				dsum = dsum + c6

			if dsum > 21:
				print "Dealer's final sum is",dsum,"\n"
				print "Dealer bust! You win!" "\n"
				money = money + b
				print "You now have $",money,"in your bank."
			elif dsum < psum:
				print "Dealer's final sum is",dsum,"\n"
				print "You win!" "\n"
				money = money + b
				print "You now have $",money,"in your bank."
			elif dsum == psum:
				print "Dealer's final sum is",dsum,"\n" 
				print "Draw." "\n"
				print "You have $",money,"in your bank."
			else:
				print "Dealer's sum is",dsum,"\n"
				print "You lose." "\n"
				money = money - b
				print "You now have $",money,"in your bank."


		yn = raw_input("Would you like to play again? (y or n): ")

		"""if "y" in yn:
			print "\n" * 5
			run()
		else:
			print "\n" "Your total winnings is $",money,
			sys.exit()  """ 
		


def main():
	print"Welcome to Black Jack Game"
	names=[]
	number=games3.ask_number("How Many Players?(1-7): ",low=1, high=8)
	print number
	for i in range(number):
		name=raw_input("Enter the player's Name: ")
		names.append(name)
	#print()
	game=BJ_Game(names) #game is the object of BJ_Game
	again=None
	while again!="n":
		game.play()
		game.run()
		
		again=games3.ask_yes_no("Do you want to play again?: ")
		#if "y" in again:
			#game.run()
		
	print "\n" "Your total winnings is $",money,
	sys.exit()
			
		


main()
input("Press Enter to exit")