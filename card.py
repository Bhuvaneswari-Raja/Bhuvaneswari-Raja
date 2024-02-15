import random

suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

class card():
	def __init__(self,suit,value):
		self.suit = suit
		self.value = value
		self.score()

	def score(self):
		if self.value == 1:
			self.score = 11
		elif self.value > 10:
			self.score = 10
		else :
			self.score = self.value

	def string(self):
		if self.value == 11:
			first_part = 'Jack'
		elif self.value == 12:
			first_part = 'Queen'
		elif self.value == 13:
			first_part = 'King'
		elif self.value == 1:
			first_part = 'Ace'
		else:
			first_part = str(self.value)
		return first_part + ' of ' + self.suit



class Deck():
	def __init__(self):
		self.dealer = []
		for suit in suits:
			for x in range(1,14):
				self.dealer.append(card(suit, x))
	def number(self):
		deck_value = ''
		for card in self.dealer:
			deck_value += card.string() + '\n'
		return 'The deck has ' + deck_value 

	def shuffle(self):
		copy = []
		while len(self.dealer) > 0:
			r = random.randint(0,len(self.dealer)-1)
			self.dealer.remove(r)

deck = Deck()
print(deck.number())





