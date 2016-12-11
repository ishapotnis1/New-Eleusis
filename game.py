#Put your program name in place of program_name

#from program_name import *
from random import randint
from new_eleusis import *
from rule import *
from prune import *
global game_ended
game_ended = False

def set_rule(rule):
    return rule

def generate_random_card():
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["S", "H", "D", "C"]
    return values[randint(0, len(values)-1)] + suits[randint(0, len(suits)-1)]

class Player(object):
    def __init__(self):
        self.hand = [generate_random_card() for i in range(14)]

    def play(self, hypothesis,cards):
        """
        'cards' is a list of three valid cards to be given by the dealer at the beginning of the game.
        Your scientist should play a card out of its given hand OR return a rule, not both.
        'game_ended' parameter is a flag that is set to True once the game ends. It is False by default
        """
        print "player play"
        return scientist(hypothesis,correct[(len(correct)-3):len(correct)], self.hand, game_ended)


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
rule = "if(greater(prev,current),True, False)"
#setRule(rule)

# The three cards that adhere to the rule
cards = ["4S", "6C", "8S"]
for i in cards:
    correct.append(i)
"""
In each round scientist is called and you need to return a card or rule.
The cards passed to scientist are the last 3 cards played.
Use these to update your board state.
"""
hypothesis=perform(cards)
flag=0
for round_num in range(14):
    # Each player plays a card or guesses a rule
    try:
        #Player 1 plays
        player_card_rule = player.play(hypothesis,cards) 
        if is_card(player_card_rule) and flag<2:
            del cards[0]
            cards.append(player_card_rule)
            test=correct[(len(correct)-2):len(correct)]
            test.append(player_card_rule)
            p=parse(rule).evaluate(test)
            print "evaluate",p
            if p==True or p=='True':
                flag+=1
                print "player correct",correct, "flag",flag
                correct.append(player_card_rule)
            else:
                flag=0
                wrong.append(player_card_rule)
                print "player wrong",wrong
                hypothesis=prune(hypothesis,correct)
                print "adv",hypothesis
        else:
            print "OUR RULE:", "if(",hypothesis,",True)"
            raise Exception('')

        #Adversary 1 plays
        ad1_card_rule = adversary1.play()
        if is_card(ad1_card_rule):
            del cards[0]
            cards.append(ad1_card_rule)
            test=correct[(len(correct)-2):len(correct)]
            test.append(ad1_card_rule)
            p=parse(rule).evaluate(test)
            print "ad1",ad1_card_rule
            print "evaluate",p
            if p==True or p=='True':
                correct.append(ad1_card_rule)
                print "adversary1",correct
                hypothesis=prune(hypothesis,correct)
                print "ad1 prune",hypothesis
            else:
                wrong.append(ad1_card_rule)
                print "ad1 wrong",wrong
                #hypothesis=prune(hypothesis,correct)
            #print cards
        else:
            print "saale 1 ko mil gya"
            print "bechara hamara rule","if(",hypothesis,",True)"
            raise Exception('')

        #Adversary 2 plays
        ad2_card_rule = adversary2.play()
        if is_card(ad2_card_rule):
            del cards[0]
            cards.append(ad2_card_rule)
            test=correct[(len(correct)-2):len(correct)]
            test.append(ad2_card_rule)
            p=parse(rule).evaluate(test)
            print "ad2",ad2_card_rule
            print "evaluate",p

            if p==True or p=='True':
                correct.append(ad2_card_rule)
                print "adversary1",correct
                hypothesis=prune(hypothesis,correct)
                print "ad1 prune",hypothesis
               
            else:
                wrong.append(ad2_card_rule)
                
            #print cards
        else:
            print "saale 2 ko mil gya"
            print "bechara hamara rule","if(",hypothesis,",True)"
            raise Exception('')

        #Adversary 3 plays
        ad3_card_rule = adversary3.play()
        if is_card(ad3_card_rule):
            del cards[0]
            cards.append(ad3_card_rule)
            test=correct[(len(correct)-2):len(correct)]
            test.append(ad3_card_rule)
            p=parse(rule).evaluate(test)
            print "ad3",ad3_card_rule
            if p==True or p=='True':
                correct.append(ad3_card_rule)
                hypothesis=prune(hypothesis,correct)
                print "ad3 prune",hypothesis
                print "evaluate",p

            else:
                wrong.append(ad3_card_rule)
                
            #print cards
        else:
            print "saale 3 ko mil gya"
            print "bechara hamara rule","if(",hypothesis,",True)"
            raise Exception('')

    except:
        game_ended = True
        break

# Everyone has to guess a rule
#rule_player = player.play(cards)

# Check if the guessed rule is correct and print the score
#score(player)
