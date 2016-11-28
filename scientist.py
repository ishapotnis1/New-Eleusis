#alternate
#AND_OR    
from new_eleusis import *
#from card_generator import *
import CurrentBestHypothesis
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

def probability(previous2,previous1,current,comparison):
    d = {'is_suit':{'D':0.25,'H':0.25,'S':0.25,'C':0.25},'is_value':{'even':0.14,'odd':0.14,'royal':0.14,'less':0.14,'greater':0.14,'plus1':0.14,'minus1':0.14},'is_color':{'R':0.5,'B':0.5}}

    #previous2
    if(previous2['D']==1):
        d['is_suit']['D']+=0.005
    if(previous2['D']==0):
        d['is_suit']['D']=d['is_suit']['D']-(0.005/(3))
                                                     
    if(previous2['H']==1):
        d['is_suit']['H']+=0.005
        #count_suit+=1
    if(previous2['H']==0):
        d['is_suit']['H']=d['is_suit']['H']-(0.005/(3))

    if(previous2['S']==1):
        d['is_suit']['S']+=0.005
        #count_suit+=1
    if(previous2['S']==0):
        d['is_suit']['S']=d['is_suit']['S']-(0.005/(3))

    if(previous2['C']==1):
        d['is_suit']['C']+=0.005
        #count_suit+=1
    if(previous2['C']==0):
        d['is_suit']['C']=d['is_suit']['C']-(0.005/(3))
                                                         
    if(previous2['R']==1):
        d['is_color']['R']+=0.005
        # count_suit+=1
    if(previous2['R']==0):
        d['is_color']['R']=d['is_color']['R']-0.005

    if(previous2['B']==1):
        d['is_color']['R']+=0.005
        # count_suit+=1
    if(previous2['B']==0):
        d['is_color']['B']=d['is_color']['B']-0.005    
        



    #previous1
    if(previous1['D']==1):
        d['is_suit']['D']+=0.005
    if(previous1['D']==0):
        d['is_suit']['D']=d['is_suit']['D']-(0.005/(3))
                                                     
    if(previous1['H']==1):
        d['is_suit']['H']+=0.005
        #count_suit+=1
    if(previous1['H']==0):
        d['is_suit']['H']=d['is_suit']['H']-(0.005/(3))

    if(previous1['S']==1):
        d['is_suit']['S']+=0.005
        #count_suit+=1
    if(previous1['S']==0):
        d['is_suit']['S']=d['is_suit']['S']-(0.005/(3))

    if(previous1['C']==1):
        d['is_suit']['C']+=0.005
        #count_suit+=1
    if(previous1['C']==0):
        d['is_suit']['C']=d['is_suit']['C']-(0.005/(3))
                                                         
    if(previous1['R']==1):
        d['is_color']['R']+=0.005
        # count_suit+=1
    if(previous1['R']==0):
        d['is_color']['R']=d['is_color']['R']-0.005

    if(previous1['B']==1):
        d['is_color']['R']+=0.005
        # count_suit+=1
    if(previous1['B']==0):
        d['is_color']['B']=d['is_color']['B']-0.005



    #current
    if(current['D']==1):
        d['is_suit']['D']+=0.005
    if(current['D']==0):
        d['is_suit']['D']=d['is_suit']['D']-(0.005/(3))
                                                     
    if(current['H']==1):
        d['is_suit']['H']+=0.005
        #count_suit+=1
    if(current['H']==0):
        d['is_suit']['H']=d['is_suit']['H']-(0.005/(3))

    if(current['S']==1):
        d['is_suit']['S']+=0.005
        #count_suit+=1
    if(current['S']==0):
        d['is_suit']['S']=d['is_suit']['S']-(0.005/(3))

    if(current['C']==1):
        d['is_suit']['C']+=0.005
        #count_suit+=1
    if(current['C']==0):
        d['is_suit']['C']=d['is_suit']['C']-(0.005/(3))
                                                         
    if(current['R']==1):
        d['is_color']['R']+=0.005
        # count_suit+=1
    if(current['R']==0):
        d['is_color']['R']=d['is_color']['R']-0.005

    if(current['B']==1):
        d['is_color']['R']+=0.005
        # count_suit+=1
    if(current['B']==0):
        d['is_color']['B']=d['is_color']['B']-0.005

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

from card_generator import *
def main():
    if len(l)!=0:
        previous2 = extraction(l[0])
        previous1 = extraction(l[1])
        current = extraction(l[2])
        correct.append(l[0])
        correct.append(l[1])
        correct.append(l[2])
        print "correct",correct
        comparison = comparator(previous2, previous1, current)
        p = probability(previous2, previous1, current, comparison)
        # print "for first three cards"
        # print comparison
        # print p
        RetCur={}
        RetCur=CurrentBestHypothesis.current_best_hypothesis(p)
        print "-------------------------------------",RetCur
        for i in range(0,10):
            card = card_generator(RetCur[0],RetCur[1])
            print "card",card
            correct_wrong(card)
            card1 = extraction(card)
            previous2 = previous1
            previous1 = current
            current = card1
            comparison1 = comparator(previous2, previous1, current)
            p1 = probability(previous2, previous1, current, comparison)
            a1 = alternate(previous2, previous1, current, comparison)
            print p1
            cb=CurrentBestHypothesis.current_best_hypothesis(p1)
        """print "count" ,CurrentBestHypothesis.count
        if CurrentBestHypothesis.count==3:

         for field, possible_values in  currentBestHypothesis.iteritems():
          for a, x in possible_values.iteritems():
           print "hereeeeee",field, a"""





if __name__ == "__main__":
 main()
