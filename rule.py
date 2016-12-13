from new_eleusis import *
from Main import *
from random import randint
def generate_random_cards():
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["S", "H", "D", "C"]
    return values[randint(0, len(values)-1)] + suits[randint(0, len(suits)-1)]

def play(g_rule,correct):   #returns whether card is legal or not
      test=correct[(len(correct)-2):len(correct)]
      test.append(player_card_rule)
      p=parse(g_rule).evaluate(test)
      return p
    
    
def scientist(data, cards, hand, game_ended):
    card_dict = []
    current_hand = [hand[0], cards[2], cards[1]]
    current  = hand[0]
    previous = cards[2] #replace with card from corrent list later
    previous2 = cards[1]
    #print "data",data
    #data = "orf(even(current),equal(color(current),R),greater(prev,current)) "
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
                #card_dict.append('color')
                card_dict.append('R')
            else:
                #card_dict.append('color :B')
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
        #print "hello",card_dict
        best_dict= {}
        for card in range(0,14):
            extr = extraction(hand[card])
            choice_score = 0
            for j in range(len(card_dict)):
                if card_dict[j] in extr.keys() and extr[card_dict[j]] == 1:
                    choice_score = choice_score + 1
                if card_dict[j] == 'greater':
                    if(greater(previous, hand[card])):
                        choice_score = choice_score + 1
                if card_dict[j] == 'less':
                    if(less(previous, hand[card])):
                        choice_score = choice_score + 1
            #print choice_score
            best_dict[hand[card]] = choice_score

    elif 'andf' in data:
        print "hi"
    elif 'iff' in data:
        print "hold"
    card = 0
    #print "hand",hand
    #print "best",best_dict
    #print max(best_dict.values())
    for k,v in best_dict.items():
        if v==max(best_dict.values()):
            #print "card gen",k
            selected=k
            break
    #print "after"
    hand.remove(selected)
    #print "rem",hand
    r = [generate_random_cards() for i in range(14)]
    #print "r",r
    hand.append(r[0])
    #print "ad",hand,selected
    if game_ended==False:
        return selected
    else:
        return data
    #break
    #self.hand.pop(k)
    #print self.hand
    #return scientist(cards, self.hand, game_ended)
    #p=parse(rule).evaluate(cards)
    #return p
    #t=Tree(p.root)
    #print t

def perform(cards):
    #rule= If (equal(suit(current), suit(prev)), greater(value(current), value(prev)), True)
    prev2=cards[0]
    prev1=cards[1]
    current=cards[2]
    list=[]
    str1="orf("
    #all even
    if even(prev2)==True and even(prev1)==True and even(current)==True:
        #all are even
        print "all even"
        list.append("even(current)")
    """elif even(prev2)==True and even(current)==True:
        print "alternate even"
        list.append("equal(even(previous2),even(current))")"""

    #all are odd
    if odd(prev2)==True and odd(prev1)==True and odd(current)==True:
        #all are odd
        print "all odd"
        list.append("odd(current)")
    """elif odd(prev2)==True and odd(current)==True:
        print "alternate odd"
        list.append("equal(odd(previous2),odd(current))")"""

    #all are royal
    if is_royal(prev2)==True and is_royal(prev1)==True and is_royal(current)==True:
        #all are royal
        print "all royal"
        list.append("is_royal(current)")
    """elif is_royal(prev2)==True and is_royal(current)==True:
        print "alternate is_royal"
        list.append("equal(is_royal(previous2),is_royal(current))")"""

    #all have same color
    if equal(color(prev2),color(prev1)) and equal(color(prev1),color(current)):
        #all are red
        print "all same color"
        if equal(color(prev2),'R')==True:
            print "all red"
            list.append("equal(color(current),R)")
        else:
            print "all black"
            list.append("equal(color(current),B)")

    #all belong to the same suit
    if equal(suit(prev2),suit(prev1)) and equal(suit(prev1),suit(current)):
        print "same suit"
        if equal(suit(current),'C'):
            print "all clubs"
            list.append("equal(suit(current),C)")
        elif equal(suit(current),'H'):
            print "all hearts"
            list.append("equal(suit(current),H)")
        elif equal(suit(current),'S'):
            print "all spades"
            list.append("equal(suit(current),S)")

        else:
            print "all diamonds"
            list.append("equal(suit(current),D)")

    if less(prev2,prev1)==True:
        if less(prev1,current)==True:
            #alternate less
            if value(prev2)<value(prev1) and value(prev1)<value(current):
                list.append("less(value(prev),value(current))")
            else:
                list.append("less(prev,current)")
            print "next card is greater than prev"

    if greater(prev2,prev1)==True:
        if greater(prev1,current)==True:
            if value(prev2)>value(prev1) and value(prev1)>value(current):
                list.append("greater(value(prev),value(current))")
            else:
                list.append("greater(prev,current)")
            #alternate greater
            print "next card is less than the previous"

    if is_royal(prev2)==False and is_royal(prev1)==False and is_royal(current)==False:
        print "no royal"
        list.append("notf(is_royal(current))")

    for i in list:
        str1+=i+","
    str1=str1[:len(str1)-1]
    str1+=")"
    return str1

