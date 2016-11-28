#alternate
#AND_OR    
from new_eleusis import *
#from card_generator import *
import CurrentBestHypothesis
#import alternate_card_generator
correct = []
wrong=[]
l=['5S','6D','8C']
#global prevres

prevres=None

def correct_wrong(card):
    print "?????",prevres
    #print "hbh",CurrentBestHypothesis.count
    x=raw_input("Press 'Y' if card is correct |  Press 'N' if card is wrong")
    if(x=='Y'):
        correct.append(card)
    else:
        wrong.append(card)
        
        
def extraction(card):
    #dict = dict{}
    value1=value(card)
    #number=value_to_number(value)
    suit1=suit(l[1])
    rules=['D','H','S','C','even','odd','royal','R','B','value','card']#'less','greater','plus1','minus1','R','B']
    #updating rules dictionary
    hypothesis={}
    #for i in range(0,len(rules)):
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
        #print 'bye'
    else:
        hypothesis[rules[4]]=0
    if(odd(card)==True):
        hypothesis[rules[5]]=1
        #print 'hello'
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
    if(less(previous2['card'],previous1['card']) and less(previous1['card'],current['card'])):
        hypothesis[rules[0]] = 1
    else:
        hypothesis[rules[0]] = 0
    if(greater(previous2['card'],previous1['card']) and greater(previous1['card'],current['card'])):
        hypothesis[rules[1]] = 1
    else:
        hypothesis[rules[1]] = 0
    if(plus1(previous2['card'])== previous1['card'] and plus1(previous1['card']) == current['card']):
        hypothesis[rules[2]] = 1
    else:
        hypothesis[rules[2]] = 0
    if(minus1(previous2['card']) == previous1['card'] and minus1(previous1['card']) == current['card']):
        hypothesis[rules[3]] = 1
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
        #count_suit+=1
    if(card['C']==0):
        d['is_suit']['C']=d['is_suit']['C']-(0.005/(3))
                                                         
    if(card['R']==1):
        d['is_color']['R']+=0.005
        # count_suit+=1
    if(card['R']==0):
        d['is_color']['R']=d['is_color']['R']-0.005

    if(card['B']==1):
        d['is_color']['R']+=0.005
        # count_suit+=1
    if(card['B']==0):
        d['is_color']['B']=d['is_color']['B']-0.005
    if(card['even'] == 1):
        d['is_value']['even'] = d['is_value']['even'] + (0.005/3)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/18)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/18)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/18)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/18)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/18)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/18)
        
    if(card['royal'] == 1):
        d['is_value']['royal'] = d['is_value']['royal'] + (0.005/3)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/18)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/18)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/18)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/18)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/18)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/18)        

    if(card['odd'] == 1):
        d['is_value']['odd'] = d['is_value']['odd'] + (0.005/3)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/18)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/18)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/18)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/18)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/18)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/18)
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
  '''  if len(l)!=0:
        for i in l:
            correct.append(i)
            previous.append(i)
        x=len(correct)
        while len(previous)<=3:
           # card=card_generator({},{})
            correct_wrong(card)
            if len(correct)>x:
                previous.append(card)
                x+=1    
    else:
        card=""
        previous=[]
        x=len(correct)
        while len(previous) <= 3:
          #  card=card_generator({},{})
            correct_wrong(card)
            if len(correct)>x:
                previous.append(card)
                x+=1    '''
    previous2=previous[0]
    previous1=previous[1]
    current=previous[2]
    print "correct",correct
    for i in range(0,10):
        comparison = comparator(previous2, previous1, current)
        p1 = probabilityCard(previous2,d)
        p2 = probabilityCard(previous1,p1)
        p3 = probabilityCard(current,p2)
        p = probabilityCompare(comparison, p3)
        a1 = alternate(previous2, previous1, current)
        altPos = alternatePos(previous2, previous1, current)
        print altPos
        cb=CurrentBestHypothesis.current_best_hypothesis(p)
        if len(a1)==0:
            card = card_generator.card_generator(cb[0],cb[1])
            print "card",card
            correct_wrong(card)
            card1 = extraction(card)
            previous2 = previous1
            previous1 = current
            current = card1
        else:
            card=card_generator.card_generator(cb[0],cb[1])#alternate_card_generator.alternateCard(a1)
            print "card",card
            correct_wrong(card)
            card1 = extraction(card)
            previous2 = previous1
            previous1 = current
            current = card1
        # print "for first three cards"
        # print comparison
        # print p
        """print "count" ,CurrentBestHypothesis.count
        if CurrentBestHypothesis.count==3:

         for field, possible_values in  currentBestHypothesis.iteritems():
          for a, x in possible_values.iteritems():
           print "hereeeeee",field, a"""




if __name__ == "__main__":
 main()
