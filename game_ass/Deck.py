import random


class deck_of_cards:
    def __init__(self, suits, values):
        self.suits = suits
        self.values = values
    
    def deck(self):
        my_deck = []
        for s in self.suits:
            for v in self.values:
                my_deck.append("{} {}".format(v,s))
        return my_deck

        
    def distribute_card(self,deck,player_cards):
        if len(deck) < 1:
            #print("It should work")
            return 0
        else:
            random.shuffle(deck)
            for x in player_cards:
                player_cards[x].append(deck.pop())
                #print("Cards remaining:",len(deck))
                
            self.distribute_card(deck,player_cards)
            
