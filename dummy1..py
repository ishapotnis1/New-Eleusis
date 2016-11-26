#alternate
#AND_OR    
from new_eleusis import *

correct = []
wrong=[]
l=['5S','6D','8C']
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
    if(color(card)=='R'):
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
previous2 = extraction(l[0])
#print previous2['card']
previous1 = extraction(l[1])
current = extraction(l[2])
comparison = comparator(previous2,previous1,current) 
print l[1]
print comparison
def probability(previous2,previous1,current,comparison):
    d = {'is_suit':{'D':0.25,'H':0.25,'S':0.25,'C':0.25},'is_value':{'even':0.14,'odd':0.14,'royal':0.14,'less':0.14,'greater':0.14,'plus1':0.14,'minus1':0.14},'is_color':{'R':0.5,'B':0.5}}
    
    rerturn d



