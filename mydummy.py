#alternate
#AND_OR    
from new_eleusis import *

correct = []
wrong=[]
l=['4S','6D','8S']
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

def probability(previous2,previous1,current,comparison):
    d = {'is_suit':{'D':0.25,'H':0.25,'S':0.25,'C':0.25},'is_value':{'even':0.14,'odd':0.14,'royal':0.14,'less':0.14,'greater':0.14,'plus1':0.14,'minus1':0.14},'is_color':{'R':0.5,'B':0.5}}
    if(previous2['even'] == 1):
        d['is_value']['even'] = d['is_value']['even'] + (0.005/3)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/18)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/18)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/18)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/18)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/18)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/18)
    if(previous1['even'] == 1):
        d['is_value']['even'] = d['is_value']['even'] + (0.005/3)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/18)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/18)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/18)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/18)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/18)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/18)
    if(current['even'] == 1):
        d['is_value']['even'] = d['is_value']['even'] + (0.005/3)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/18)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/18)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/18)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/18)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/18)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/18)
    if(previous2['royal'] == 1):
        d['is_value']['royal'] = d['is_value']['royal'] + (0.005/3)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/18)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/18)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/18)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/18)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/18)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/18)
    if(previous1['royal'] == 1):
        d['is_value']['royal'] = d['is_value']['royal'] + (0.005/3)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/18)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/18)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/18)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/18)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/18)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/18)
    if(current['royal'] == 1):
        d['is_value']['royal'] = d['is_value']['royal'] + (0.005/3)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/18)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/18)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/18)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/18)
        d['is_value']['odd'] = d['is_value']['odd'] - ((0.005)/18)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/18)
    if(previous2['odd'] == 1):
        d['is_value']['odd'] = d['is_value']['odd'] + (0.005/3)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/18)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/18)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/18)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/18)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/18)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/18)
    if(previous1['odd'] == 1):
        d['is_value']['odd'] = d['is_value']['odd'] + (0.005/3)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/18)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/18)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/18)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/18)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/18)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/18)
    if(current['odd'] == 1):
        d['is_value']['odd'] = d['is_value']['odd'] + (0.005/3)
        d['is_value']['greater'] = d['is_value']['greater'] - ((0.005)/18)
        d['is_value']['plus1'] = d['is_value']['plus1'] - ((0.005)/18)
        d['is_value']['minus1'] = d['is_value']['minus1'] - ((0.005)/18)
        d['is_value']['less'] = d['is_value']['less'] - ((0.005)/18)
        d['is_value']['even'] = d['is_value']['even'] - ((0.005)/18)
        d['is_value']['royal'] = d['is_value']['royal'] - ((0.005)/18)
    
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

def alternate(previous2,previous1,current,comparison):
    alter = {}
    for key in previous2:
        if (previous2.get(key) == current.get(key) and current.get(key) == 1):
            alter[key] = [];
            for k in previous1:
                if (previous1[k] == 1):
                    alter[key].append(k)
    return alter
#alternate suit, color , number

previous2 = extraction(l[0])
previous1 = extraction(l[1])
current = extraction(l[2])
comparison = comparator(previous2,previous1,current) 
prob = probability(previous2,previous1,current,comparison)
alt = alternate(previous2,previous1,current,comparison)
print alt



