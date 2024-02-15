import random

suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

class card():
	def __init__(self,suit,value):
		self.suit = suit
		self.value = value
		self.score()

	def score():
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
			return first_part + 'of' + self.suits
			
