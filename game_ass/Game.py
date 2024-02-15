class game():
    
    def __init__(self,players):
        self.players = players
        
    def first_round(self,finished,players,highest_card):
        temp_list = []
        card = 0
        while len(highest_card) < 1 and len(temp_list) < 5:
            for x in players:
                if "ACE S" in players[x]:
                    print(x,"has Ace of S")
                    temp_list.append(players[x].pop(players[x].index("ACE S")))
                    highest_card = x
                    last_player = highest_card
                    
            for person in players:
                if highest_card == person:
                    continue
                print(person,":",players[person])
                player_choice = input("Enter your card: ")
                if player_choice in players[person]:
                    if player_choice[-1] != temp_list[-1][-1]:
                        temp_list.append(player_choice)
                        self.card_cutting(temp_list,players,person,last_player,player_choice)
                        print(person,":",players[person])
                        player_choice = input("Enter your card: ")
                        if player_choice in players[person]:
                            temp_list.append(players[person].pop(players[person].index(player_choice)))
                        else:
                            self.wrong_card(person,players[person],players)
                    else:
                        if player_choice in players[person]:
                            temp_list.append(players[person].pop(players[person].index(player_choice)))
                        else:
                            self.wrong_card(person,players[person],players)
                        
                    #temp_list.append(players[person].pop(players[person].index(player_choice)))
                else:
                    self.wrong_card(person,players[person],players)
                last_player = person
                #card += 1
        highest_card = self.find_highest_card(temp_list)
        self.game_play(finished,players,highest_card)

    
    def game_play(self, finished,players,highest_card):
        temp_list = []
        winner = False
        last_player = highest_card
        while winner == False:
            print("----------------------------------------------------------------------")
            print(highest_card,"had the highest card last round")
            print(highest_card,":",players[highest_card])
            player_choice = input("Enter your card: ")
            if player_choice in players[highest_card]:
                if len(temp_list) >= 1:
                    if temp_list[-1][-1] != player_choice[-1]:
                        temp_list.append(player_choice)
                        self.card_cutting(temp_list,players,highest_card,last_player,player_choice)
                        print(highest_card,":",players[highest_card])
                        player_choice = input("Enter your card: ")
                        if player_choice in players[highest_card]:
                            temp_list.append(players[highest_card].pop(players[highest_card].index(player_choice)))
                        else:
                            self.wrong_card(highest_card,players[highest_card],players)
                else:
                    if player_choice in players[highest_card]:
                        temp_list.append(players[highest_card].pop(players[highest_card].index(player_choice)))
                    else:
                        self.wrong_card(highest_card,players[highest_card],players)

            for person in players:
                if highest_card == person:
                    continue        
                print(person,":",players[person])
                player_choice = input("Enter your card: ")
                if player_choice in players[person]:
                    if len(temp_list) >=1:
                        if temp_list[-1][-1] != player_choice[-1]:
                            temp_list.append(player_choice)
                            self.card_cutting(temp_list,players,person,last_player,player_choice)
                            print(person,":",players[person])
                            player_choice = input("Enter your card: ")
                            if player_choice in players[person]:
                                temp_list.append(players[person].pop(players[person].index(player_choice)))
                            else:
                                self.wrong_card(person,players[person],players)
                    else:
                        if player_choice in players[person]:
                            temp_list.append(players[person].pop(players[person].index(player_choice)))
                        else:
                            self.wrong_card(person,players[person],players)
                        
                    #temp_list.append(players[person].pop(players[person].index(player_choice)))
                else:
                    self.wrong_card(person,players[person],players)
                last_player = person
            highest_card = self.find_highest_card(temp_list)
            finished.append(temp_list)
                    
        """
        while winner == False:
            print("-------------------------------------------")
            for person in players:
                if person != highest_card:
                    continue
                print()
                print(person,"':",players[person])
                print(person,end=" ")
                player_choice = str(input("Enter your card: "))
                temp = player_choice.split()
                if  temp[1]== "S":
                    temp[1] = "\u2660"
                    #print(" ".join(temp))
                    temp = " ".join(temp)
                    if temp in players[person]:
                        #print("It works")
                        temp_list.append(players[person].pop(players[person].index(temp)))
                if  temp[1]== "C":
                    temp[1] = "\u2663"
                    temp = " ".join(temp)
                    if temp in players[person]:
                        #print("It works")
                        temp_list.append(players[person].pop(players[person].index(temp)))
                if  temp[1]== "D":
                    temp[1] = "\u2666"
                    temp = " ".join(temp)
                    if temp in players[person]:
                        #print("It works")
                        temp_list.append(players[person].pop(players[person].index(temp)))
                if  temp[1]== "H":
                    temp[1] = "\u2665"
                    temp = " ".join(temp)
                    if temp in players[person]:
                        #print("It works")
                        temp_list.append(players[person].pop(players[person].index(temp)))
            
            for human in players:
                if human == highest_card:
                    continue
                print()
                print(human,"':",players[human])
                print(human,end=" ")
                player_choice = str(input("Enter your card: "))
                temp = player_choice.split()
                if  temp[1]== "S":
                    temp[1] = "\u2660"
                    temp = " ".join(temp)
                    if temp in players[human]:
                        temp_list.append(players[human].pop(players[human].index(temp)))
                if  temp[1]== "C":
                    temp[1] = "\u2663"
                    temp = " ".join(temp)
                    if temp in players[human]:
                        temp_list.append(players[human].pop(players[human].index(temp)))
                if  temp[1]== "D":
                    temp[1] = "\u2666"
                    temp = " ".join(temp)
                    if temp in players[human]:
                        temp_list.append(players[human].pop(players[human].index(temp)))
                if  temp[1]== "H":
                    temp[1] = "\u2665"
                    temp = " ".join(temp)
                    if temp in players[human]:
                        temp_list.append(players[human].pop(players[human].index(temp)))
            
            my_list.append(temp_list)
            #print("Cards this rounds:",temp_list)
            highest_card = input("Who played the higest card? ")
            winner = self.determine_winner(players)
            """          
        
    def determine_winner(self,players):
        for x in players:
            if len(players[x]) < 1:
                return True
            
    def wrong_card(self,name,temp,players):
        print("Enter valid card")
        print(name,":",players[name])
        card = input("Enter your card: ")

        while card not in players[name]:
            print("Enter valid card")
            print(name,":",players[name])
            card = input("Enter your card: ")
            
        temp(players[name].pop(players[name].index(card))) 

        
    def card_cutting(self,round_list,players,current_player,previous_player,current_card):
        print(current_player,"is card cutting")
        players[current_player].remove(current_card)

        for x in round_list:
            players[previous_player].append(x)
        round_list.clear()
        
    def find_highest_card(self,round_cards):
       highest_card = max(round_cards)
       return highest_card