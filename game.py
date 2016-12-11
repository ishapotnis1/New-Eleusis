#Put your program name in place of program_name

from eleusis import *
from random import randint
from new_eleusis import *
import re

from scientist import *

global game_ended
game_ended = False

def generate_random_card():
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["S", "H", "D", "C"]
    return values[randint(0, len(values)-1)] + suits[randint(0, len(suits)-1)]

hypo = "orf(even(current),equal(color(current),R),greater(prev,current))"
class Player(object):

    def __init__(self):
        #self.card=[]
        self.hand = [generate_random_card() for i in range(0,14)]
        self.card = []
        '''
        self.card[0] = extraction(self.hand[0])
        self.card[1] = extraction(self.hand[1])
        self.card[2] = extraction(self.hand[2])
        self.card[3] = extraction(self.hand[3])
        self.card[4] = extraction(self.hand[4])
        self.card[5] = extraction(self.hand[5])
        self.card[6] = extraction(self.hand[6])
        self.card[7] = extraction(self.hand[7])
        self.card[8] = extraction(self.hand[8])
        self.card[9] = extraction(self.hand[9])
        self.card[10] = extraction(self.hand[10])
        self.card[11] = extraction(self.hand[11])
        self.card[12] = extraction(self.hand[12])
        self.card[13] = extraction(self.hand[13])
        '''

    def play(self, cards):
        """
        'cards' is a list of three valid cards to be given by the dealer at the beginning of the game.
        Your scientist should play a card out of its given hand OR return a rule, not both.
        'game_ended' parameter is a flag that is set to True once the game ends. It is False by default
        """
        card_dict = []
        current_hand = [self.hand[0], cards[2], cards[1]]
        current  = self.hand[0]
        previous = cards[2] #replace with card from corrent list later
        previous2 = cards[1]
        data = "orf(even(current),equal(color(current),R),greater(prev,current)) "
        if 'orf' in data:
            data = data.split('orf(')[1]
            data = data.rsplit(')', 1)[0]
            #data = data.split("),")
            if 'even' in data:
                card_dict.append('even')
            if 'odd' in data:
                card_dict.append('odd')
            if 'is_royal' in data:
                card_dict.append('is_royal')
            if 'color' in data:
                if 'R),' in data:
                    card_dict.append('color')
                    card_dict.append('R')
                else:
                    card_dict.append('color :B')
                    card_dict.append('B')
            if 'suit' in data:
                if 'H),' in data:
                    card_dict.append('suit')
                    card_dict.append('H')
                elif 'C),' in data:
                    card_dict.append('suit :C')
                    card_dict.append('C')
                elif 'D),' in data:
                    card_dict.append('suit :D')
                    card_dict.append('D')
                elif 'S),' in data:
                    card_dict.append('suit :S')
                    card_dict.append('S')
            if 'greater' in data:
                card_dict.append('greater')
            if 'less' in data:
                card_dict.append('less')
            print "hello",card_dict
            best_dict= {}
            for  card in range(0,14):
                extr = extraction(self.hand[card])
                choice_score = 0
                for j in range(len(card_dict)):
                    if card_dict[j] in extr.keys() and extr[card_dict[j]] == 1:
                        choice_score = choice_score + 1
                    if card_dict[j] == 'greater':
                        if(greater(previous, self.hand[card])):
                            choice_score = choice_score + 1
                    if card_dict[j] == 'less':
                        if(less(previous, self.hand[card])):
                            choice_score = choice_score + 1
                best_dict[self.hand[card]] = choice_score

        elif 'andf' in data:
            print "hi"
        elif 'iff' in data:
            print "hold"
        card = 0
        print self.hand
        print best_dict
        print max(best_dict.values())
        for k,v in best_dict.items():
            if v==max(best_dict.values()):
                print k
                break
        #self.hand.pop(k)
        #print self.hand
        #return scientist(cards, self.hand, game_ended)
        p=parse(rule).evaluate(cards)
        print p
        #t=Tree(p.root)
        #print t
       # print t.evaluate(cards)


class Adversary(object):
    def __init__(self):
        self.hand = [generate_random_card() for i in range(14)]

    def play(self):
        """
        'cards' is a list of three valid cards to be given by the dealer at the beginning of the game.
        Your scientist should play a card out of its given hand.
        """
        # Return a rule with a probability of 1/14
        prob_list = [i for i in range(14)]
        prob = prob_list[randint(0, 13)]
        if prob == 4:
            # Generate a random rule
            rule = ""
            conditions = ["equal", "greater"]
            properties = ["suit", "value"]
            cond = conditions[randint(0,len(properties)-1)]
            if cond == "greater":
                prop = "value"
            else:
                prop = properties[randint(0,len(properties)-1)]

            rule += cond + "(" + prop + "(current), " + prop + "(previous)), "
            return rule[:-2]+")"
        else:
            return self.hand[randint(0, len(self.hand)-1)]


# The players in the game
player = Player()
adversary1 = Adversary()
adversary2 = Adversary()
adversary3 = Adversary()

# Set a rule for testing
rule = "if(is_royal(current), False, True)"
#setRule(rule)

# The three cards that adhere to the rule
cards = ["2D", "4H", "6H"]
print cards[2]
"""
In each round scientist is called and you need to return a card or rule.
The cards passed to scientist are the last 3 cards played.
Use these to update your board state.
"""
'''
for round_num in range(14):
    # Each player plays a card or guesses a rule
    try:
        #Player 1 plays
        player_card_rule = player.play()
        if is_card(player_card_rule):
            del cards[0]
            cards.append(player_card_rule)
        else :
            raise Exception('')
        

        #Adversary 1 plays
        ad1_card_rule = adversary1.play()
        if is_card(ad1_card_rule):
            del cards[0]
            cards.append(ad1_card_rule)
            #print cards
        else:
            raise Exception('')

        #Adversary 2 plays
        ad2_card_rule = adversary2.play()
        if is_card(ad2_card_rule):
            del cards[0]
            cards.append(ad2_card_rule)
            #print cards
        else:
            raise Exception('')

        #Adversary 3 plays
        ad3_card_rule = adversary3.play()
        if is_card(ad3_card_rule):
            del cards[0]
            cards.append(ad3_card_rule)
            #print cards
        else:
            raise Exception('')

    except:
        game_ended = True
        break
'''
# Everyone has to guess a rule
rule_player = player.play(cards)

# Check if the guessed rule is correct and print the score
#score(player)
