import random
import time

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
		self.shuffle()

	def number(self):
		deck_value = ''
		for card in self.dealer:
			deck_value += card.string() + '\n'
		return deck_value 

	def shuffle(self):
		copy = []
		while len(self.dealer) > 0:
			r = random.randint(0,len(self.dealer)-1)
			x = self.dealer.pop(r)
			copy.append(x)
		self.dealer = copy


class Participant():
	def __init__(self, is_dealer):
		self.hand = []
		self.is_dealer = is_dealer
		self.busted = False

	def scores(self):
		self.score = 0
		for card in self.hand:
			self.score += card.score
		if self.score > 21:
			for card in self.hand:
				if card.score == 11:
					self.score -= 10
					card.score -= 10
					if self.score <= 21:
						break
		if self.score > 21:
			self.busted = True	

	def dealer_hand(self):
		if self.is_dealer is True:
			print('Dealer hand:')
		else:
			print('Your hand: ')
		for card in self.hand:
			print(card.string(), end = "    ")
		print("")

class Game():
	def __init__(self):
		self.you = Participant(False)
		self.dealer = Participant(True)
		self.deck = Deck()
		self.hit(True)
		self.hit(False)
		self.hit(True)
		self.hit(False)

	def hit(self, is_dealer):
		if is_dealer:
			self.dealer.hand.append(self.deck.dealer.pop())
			self.dealer.scores()
		else:
			self.you.hand.append(self.deck.dealer.pop())
			self.you.scores()

	def new(self):
		self.deck= Deck()
		self.you.busted = False
		self.dealer.busted = False
		self.hit(True)
		self.hit(False)
		self.hit(True)
		self.hit(False)

	def print_game(self):
		print("-----------------------------------------------")
		time.sleep(1)
		self.you.dealer_hand()
		print(self.you.score)
		self.dealer.dealer_hand()
		print(self.dealer.score)

	def player_round(self):
		self.print_game()
		while self.you.busted == False and self.you.score != 21:
			hit_stand = input('Hit or Stand? ')

			if hit_stand == "Hit":
				self.hit(False)
				self.print_game()
			else:
				break
		if self.you.busted == True:
			print('YOU LOSE')
		elif self.you.score == 21:
			print('BLACKJACK')
		else:
			self.dealer_round()

	def dealer_round(self):
		self.print_game()
		while self.dealer.score < 17:
			self.hit(True)
			self.print_game()
		if self.dealer.busted:
			print("WINNER")
		elif self.dealer.score < self.you.score:
			print('WINNER')
		elif self.dealer.score == self.you.score:
			print('TIE')
		elif self.dealer.score > self.you.score:
			print('GAME OVER')

g = Game()
g.player_round()