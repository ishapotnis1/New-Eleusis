#Put your program name in place of program_name

from program_name import *
from random import randint
from new_eleusis import *

global game_ended
game_ended = False

def generate_random_card():
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["S", "H", "D", "C"]
    return values[randint(0, len(values)-1)] + suits[randint(0, len(suits)-1)]

class Player(object):
    def __init__(self):
        self.hand = [generate_random_card() for i in range(14)]

    def play(self, cards):
        """
        'cards' is a list of three valid cards to be given by the dealer at the beginning of the game.
        Your scientist should play a card out of its given hand OR return a rule, not both.
        'game_ended' parameter is a flag that is set to True once the game ends. It is False by default
        """
        return scientist(cards, self.hand, game_ended)


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
rule = "if(is_royal(current), False)"
setRule(rule)
# The three cards that adhere to the rule
cards = ["10H", "2C", "4S"]

for round_num in range(14):
    # Each player plays a card or guesses a rule
    try:
        if is_card(adversary1.play()) or is_card(adversary2.play()) or is_card(adversary3.play()):
            continue
        else:
            game_ended = True
            break
    except:
        game_ended = True
        break

# Everyone has to guess a rule
rule_player = player.play(cards)

# Check if the guessed rule is correct and print the score
score(player)




##################################OUR CODE :
count=0

cb={}

constraints={}
currentBestHypothesis={}
forvalidation={}
threshold=0.0

def pruning(hypothesis,correct,a1):
        k=hypothesis
        w=len(k)
        h=k.keys()
        f=[]
        q=[]
        for i in range(0,len(correct)):
                c=scientist.extraction(correct[i])
                d=c.keys()
                for i in range(0,len(d)):
                        for j in range(0,len(h)):
                                if(d[i]==h[j]):
                                        if(c[d[i]]==1):
                                                f.append(d[i])
        final1=[]
        c1=scientist.extraction(correct[0])
        c2=scientist.extraction(correct[1])
        c3=scientist.extraction(correct[2])
        d3=scientist.comparator(c1,c2,c3)
        i=3
        while(i<len(correct)):
                d2=scientist.comparator(c1,c2,c3)
                d1=d2.keys()
                for i1 in range(0,len(d1)):
                        for j in range(0,len(h)):
                                if(d1[i1]==h[j]):
                                        if(d2[d1[i1]]==1):
                                                q.append(d1[i1])
                c2=c1
                c3=c2
                c1=scientist.extraction(correct[i])
                i=i+1
                if(i==len(correct)):
                        break
        for x in q:#pruning is_color
                        #print x
                        if x not  in final1:
                                final1.append(x)
        final=[]  
        for x in f:#pruning is_color
                if x not  in final:
                        final.append(x)
        final2=[]
        final_hypo={}
        if(len(a1)!=0):
                final2=a1.keys()        
                
        best=final+final1
        final_hypo['AND of rule']=best
        final_hypo['AND of Alternate']=final2
        if(final_hypo==None):
                 y=scientist.score(scientist.scoring,30)  #Score=30 if no hypthesis match with correct list
        return final_hypo

#main scientist function
def current_best(hypothesis,flag,correct,a1,count_iter):
        temp={}
	tempconstraints={}
	tempValidation={}
	if flag==7:
                w=pruning(currentBestHypothesis,correct,a1)
                print w
                return
        else:
                for field, possible_values in hypothesis.iteritems():
                        for a,x in possible_values.iteritems():
                                if x>0.15:
                                         currentBestHypothesis[a] = x
                                if x<0.05:
                                         constraints[a] = x
                                if x<0.15and x>0.05:
                                         forvalidation[a] = x

                return forvalidation,currentBestHypothesis
        if(count_iter==20):
                w1=pruning(currentBestHypothesis,correct,a1)
                print w1
                return
                
#****** SCIENTIST.PY:
global correct
correct = []
global wrong
wrong=[]
global current
current={}
l=[]
global board_list
board_list=[]
wrong_board=[]
global alter
alter = {}
prevres=None

def score(scoring, number):
   scoring = scoring + number
   return scoring


def correct_wrong(card,flag,scoring):
    x=raw_input("Press 'Y' if card is correct |  Press 'N' if card is wrong")
    tuple1=()
    list1=[]
    if(x=='Y'):
        flag+=1
        """tuple1=list(tuple1)
        tuple1.append(card)
        for i in wrong_board:
            list1.append(i)
        tuple1.append(list1)
        print tuple1
        tuple1=tuple(tuple1)
        board_list.append(tuple1)"""
        correct.append(card)
        """if flag > 20 and flag < 200 :
           scoring = score(scoring ,1)"""
    else:
        flag=0
        wrong.append(card)
        """wrong_board.append(card)
        scoring = score(scoring ,2)"""
    return flag
            
			
def setRule(rule,alternate_rule):
    return rule,alternate_rule

			   
def extraction(card):
    value1=value(card)
    rules=['D','H','S','C','even','odd','royal','R','B','value','card']
    #updating rules dictionary
    hypothesis={}
    if(suit(card)=='D'):
        hypothesis[rules[0]]=1
    else:
        hypothesis[rules[0]]=0
    if(suit(card)=='H'):
        hypothesis[rules[1]]=1
    else:
        hypothesis[rules[1]]=0
    if(suit(card)=='S'):
        hypothesis[rules[2]]=1
    else:
        hypothesis[rules[2]]=0
    if(suit(card)=='C'):
        hypothesis[rules[3]]=1
    else:
        hypothesis[rules[3]]=0
    if(even(card)==True):
        hypothesis[rules[4]]=1
    else:
        hypothesis[rules[4]]=0
    if(odd(card)==True):
        hypothesis[rules[5]]=1
    else:
        hypothesis[rules[5]]=0
    if(is_royal(card)==True):
        hypothesis[rules[6]]=1
    else:
        hypothesis[rules[6]]=0
    if (color(card)=='R'):
        hypothesis[rules[7]]=1
    else:
         hypothesis[rules[7]]=0
    if(color(card)=='B'):
        hypothesis[rules[8]]=1
    else:
         hypothesis[rules[8]]=0
         
    hypothesis[rules[9]]=value1
    hypothesis[rules[10]]=card

    return hypothesis

#less than 3 rule pending
def comparator(previous2,previous1,current):
    rules=['less','greater','plus1','minus1']
    hypothesis ={}
    print previous2
    if(less(previous2['card'],previous1['card']) and less(previous1['card'],current['card'])):
        hypothesis[rules[0]] = 1
    else:
        hypothesis[rules[0]] = 0
    if(greater(previous2['card'],previous1['card']) and greater(previous1['card'],current['card'])):
        hypothesis[rules[1]] = 1
    else:
        hypothesis[rules[1]] = 0
    if (previous2['value']+1<14 and previous1['value']+1<14):
        if(plus1(previous2['card'])== previous1['card'] and plus1(previous1['card']) == current['card']):
            hypothesis[rules[2]] = 1
        else:
            hypothesis[rules[2]] = 0
    else:
        hypothesis[rules[2]] = 0
    if (previous2['value']-1>0 and previous1['value']-1>0):
        if(minus1(previous2['card']) == previous1['card'] and minus1(previous1['card']) == current['card']):
            hypothesis[rules[3]] = 1
        else:
            hypothesis[rules[3]] = 0

    else:
        hypothesis[rules[3]] = 0
    
    return hypothesis

def alternate(previous2,previous1,current):
    alter = {}
    for key in previous2:
        if (previous2.get(key) == current.get(key) and current.get(key) == 1):
            alter[key] = [];
            for k in previous1:
                if (previous1[k] == 1):
                    alter[key].append(k)
    return alter

def alternatePos(previous2,previous1,current):
    alterPos = {}
    for key in previous2:
        if (previous2.get(key) == current.get(key) and current.get(key) == 1):
            alterPos[key] = [];
            for k in current:
                if (current[k] == 1):
                    alterPos[key].append(k)
    return alterPos

def probabilityCard(card, d):
    if(card['D']==1):
        d['is_suit']['D']+=0.005
    if(card['D']==0):
        d['is_suit']['D']=d['is_suit']['D']-(0.005/(3))
                                                     
    if(card['H']==1):
        d['is_suit']['H']+=0.005
        #count_suit+=1
    if(card['H']==0):
        d['is_suit']['H']=d['is_suit']['H']-(0.005/(3))

    if(card['S']==1):
        d['is_suit']['S']+=0.005
        #count_suit+=1
    if(card['S']==0):
        d['is_suit']['S']=d['is_suit']['S']-(0.005/(3))

    if(card['C']==1):
        d['is_suit']['C']+=0.005
    if(card['C']==0):
        d['is_suit']['C']=d['is_suit']['C']-(0.005/(3))
                                                         
    if(card['R']==1):
        d['is_color']['R']+=0.005
    if(card['R']==0):
        d['is_color']['R']=d['is_color']['R']-0.005

    if(card['B']==1):
        d['is_color']['R']+=0.005
    if(card['B']==0):
        d['is_color']['B']=d['is_color']['B']-0.005
    if(card['even'] == 1):
        d['is_value']['even'] = d['is_value']['even'] + (0.005)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/6)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/6)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/6)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/6)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/6)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/6)
        
    if(card['royal'] == 1):
        d['is_value']['royal'] = d['is_value']['royal'] + (0.005)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/6)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/6)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/6)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/6)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/6)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/6)        

    if(card['odd'] == 1):
        d['is_value']['odd'] = d['is_value']['odd'] + (0.005)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/6)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/6)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/6)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/6)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/6)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/6)
    return d

def probabilityCompare(comparison, d):
    if (comparison['less'] == 1):
        d['is_value']['less'] = d['is_value']['less'] + (0.005)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/6)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/6)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/6)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/6)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/6)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/6)
        
    if (comparison['greater'] == 1):
        d['is_value']['greater'] = d['is_value']['greater'] + (0.005)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/6)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/6)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/6)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/6)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/6)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/6)
        
    if (comparison['plus1'] == 1):
        d['is_value']['plus1'] = d['is_value']['plus1'] + (0.005)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/6)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/6)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/6)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/6)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/6)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/6)
        
    if (comparison['minus1'] == 1):
        d['is_value']['minus1'] = d['is_value']['minus1'] + (0.005)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/6)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/6)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/6)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/6)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/6)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/6)
    return d

import card_generator
def main():
    d = {'is_suit':{'D':0.25,'H':0.25,'S':0.25,'C':0.25},'is_value':{'even':0.14,'odd':0.14,'royal':0.14,'less':0.14,'greater':0.14,'plus1':0.14,'minus1':0.14},'is_color':{'R':0.5,'B':0.5}}
    previous=[]
    current={}
    flag=0
    scoring = 0
    count_iter=0
    x=raw_input("Is the God entering any cards?(Y/N)")
    if(x=='Y'):
        more='Y'
        card=""
        while more=='Y':
            l.append(raw_input("Enter card as 3H,4B etc"))
            more=raw_input("Do you wish to enter more?(Y/N)")
        for i in l:
            previous.append(i)
            correct.append(i)
        if len(previous)<3:
            x=len(correct)
            while len(previous)!=3:
                card=card_generator.random_card()
                print card
                flag=correct_wrong(card,flag,scoring)            
                if len(correct)>x:
                    l.append(card)
                    previous.append(card)
                    x+=1                    
    #god has not given any card
    elif x=='N':
        if len(l)==0:
            card=""
            previous=[]
            #correct will b empty
            x=len(correct)
            #3 correct random cards taken
            while len(previous)<=3:
                card=card_generator.random_card()
                print card
                flag=correct_wrong(card,flag,scoring)
                if len(correct)>x:
                    l.append(card)
                    previous.append(card)
                    x+=1
    previous2=extraction(previous[0])
    previous1=extraction(previous[1])
    current=extraction(previous[2])
    a1 = alternate(previous2, previous1, current)
    for i in range(0,200):
        count_iter=count_iter+1
        comparison = comparator(previous2, previous1, current)
    
        p1 = probabilityCard(previous2,d)
        p2 = probabilityCard(previous1,p1)
        p3 = probabilityCard(current,p2)
        p = probabilityCompare(comparison, p3)
        a1 = alternate(previous2, previous1, current)
        print a1
        altPos = alternatePos(previous2, previous1, current)
        s=setRule(p,a1)
        print "setrule",s
        cb=CurrentBestHypothesis.current_best(p,flag,correct,a1,count_iter)
        if cb==None:
            print "We found the above rule! Yayy!"
            x=raw_input("Is the rule correct?(Y/N)")
            if x == 'N':
               scoring = score(scoring ,15)
            break
        if len(a1)==0:
            card = card_generator.card_generator(cb[0],cb[1],correct)
            print "card",card
            flag=correct_wrong(card,flag,scoring)
            card1 = extraction(card)
            previous2 = previous1
            previous1 = current
            current = card1
        else:
            card=alternateCardGen.alternateCard(correct)
            print "card",card
            flag=correct_wrong(card,flag,scoring)
            card1 = extraction(card)
            previous2 = previous1
            previous1 = current
            current = card1
       
"""def play(card,flag):
    print card
    flag=correct_wrong(card,flag)
    if flag==0:
        print "BoardState",boardState()
        return False
    else:
        print "BoardState",boardState()
        return True"""

def boardState():
    return board_list
