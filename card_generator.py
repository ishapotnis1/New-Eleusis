import itertools,random
avg={'D':0.4,'royal':0.3,'even':0.33}
high={'R':0.5,'odd':0.6}
visited_rules=[]
#return a royal 
def create_royal():
    royal=['J','Q','K']
    return random.choice(royal)

#return an even number
def create_even(isroyal):
    #if it is not royal then return any even number card
    if isroyal=='N':
        even=['2','4','6','8','10']
        return random.choice(even)
    else:
        #if it is royal, then return 'Q' , the only even royal card
        return 'Q'
    
#return an odd number
def create_odd(isroyal):
    #if it is not royal then return any odd number card
    if isroyal=='N':
        odd=['1','3','5','7','9']
        return random.choice(odd)
    else:
        #if it is royal, then return any card 'J' or 'K'
        odd=['J','K']
        return random.choice(odd)

#return diamond or heart if rule is red based on their probabilities      
def create_red():
    probD=0.0
    probH=0.0
    if 'D' in avg:
        probD=avg['D']
    if 'D' in high:
        probD=high['D']
    if 'H' in avg:
        probH=avg['H']
    if 'H' in high:
        probH=high['H']
    if probD>probH:
        return 'D'
    else:
        return 'H'
    
#return spade or club if rule is black based on their probabilities      
def create_black():
    probS=0.0
    probC=0.0
    if 'C' in avg:
        probC=avg['C']
    if 'C' in high:
        probC=high['C']
    if 'S' in avg:
        probS=avg['S']
    if 'S' in high:
        probS=high['S']
    if probS>probC:
        return 'S'
    else:
        return 'C'

#generate the new card   
def card_generator():
    card=""
    perm = list(itertools.product(avg.keys(), high.keys()))
    new_card=""
    for i in perm:
        #separating rules from generated permutation
        rule1,rule2=i
        #if rule1 in visited_rules and rule2
        if rule1!='even':
            if rule1!='odd':
                if rule2!='odd':
                    if rule2!='even':
                        #no even or odd rule selected and its not royal
                        if rule1!='royal' or rule2!='royal':
                            card+=str(random.randint(1,11))
                        else:
                            card+=create_royal()
                    else:
                        #second rule is even but first rule is royal
                        if rule1=='royal':
                            card+=str(create_even('Y'))
                        else:
                            card+=str(create_even('N'))     
                else:
                    #second rule is odd but first rule is royal
                    if rule1=='royal':
                        card+=str(create_odd('Y'))
                    else:
                        card+=str(create_odd('N'))
            else:
                #first rule is odd but second rule is royal
                if rule2=='royal':
                    card+=str(create_odd('Y'))
                else:
                    card+=str(create_odd('N'))
        else:
            #first rule is even but second rule is royal
            if rule2=='royal':
                card+=str(create_even('Y'))
            else:
                card+=str(create_even('N'))
            
    #one rule is royal
        if rule1=='royal' or rule2=='royal':
            #second rule is 
            card+=create_royal()
            
    #one rule is diamond
        if rule1=='D' or rule2=='D':
            #second is black
            if rule1=='B' or rule2=='B':
                continue
            else:
                card+='D'

    #one rule is heart
        if rule1=='H' or rule2=='H':
            #second is black
            if rule1=='B' or rule2=='B':
                continue
            else:
                card+='H'

    #one rule is spade
        if rule1=='S' or rule2=='S':
            #second is red
            if rule1=='R' or rule2=='R':
                continue
            else:
                card+='S'

    #one rule is club
        if rule1=='C' or rule2=='C':
            #second is red
            if rule1=='R' or rule2=='R':
                continue
            else:
                card+='C'
       
    #one rule is red
        if rule1=='R' or rule2=='R':
            #other one is black
            if rule1=='B' or rule2=='B':
                #for the case when one rule is red and other is black
                continue
            else:
                #for the case when any one of them is red
                card+=create_red()

    #one rule is black
        if rule1=='B' or rule2=='B':
            #second is red
            if rule1=='R' or rule2=='R':
                #for the case when one rule is red and other is black
                continue
            else:
                #case when one of them is black
                card+=create_black()                
        return card
    
print card_generator()
