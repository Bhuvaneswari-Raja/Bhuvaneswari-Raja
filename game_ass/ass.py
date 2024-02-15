from Deck import deck_of_cards
from Game import game

SUITS = ['H', 'D', 'C', 'S']
VALUES = ["2","3","ACE"]

#VALUES = ["2","3","4","5","6","7","8","9","ACE"]
#FACE_VALUES = {"JACK":11,"QUEEN":12,"KING":13,"ACE":14}

def before_game(players): 
    deck_obj = deck_of_cards(SUITS,VALUES)
    
    deck = deck_obj.deck()
    deck_obj.distribute_card(deck,players)
    #print(people)

def start_game(players):
    game_obj = game(players)
    finished_deck = [] 
    game_obj.first_round(finished_deck,players,"")

people = {"Raja":[],"Kala":[],"Pooja":[]}
          
before_game(people)

start_game(people)