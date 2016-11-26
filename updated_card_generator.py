import itertools,random
avg={'D':0.4,'royal':0.3,'even':0.33}
high={'H':0.55,'R':0.5,'odd':0.6}
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
    count=0
    #to keep a count of how many cards have been generated
    count+=1
    card=""
    perm = list(itertools.product(avg.keys(), high.keys()))
    random.shuffle(perm)
    new_card=""
    
    for i in perm:
        #separating rules from generated permutation
        rule1,rule2=i
        visited_rules.append(rule1)
        visited_rules.append(rule2)
        """if rule1!='even':
            if rule1!='odd':
                if rule2!='odd':
                    if rule2!='even':
                        #no even or odd rule selected and its not royal
                        if rule1!='royal' or rule2!='royal':
                            #card+=str(random.randint(1,11))
                            #if one rule is even and another is odd
                            continue
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
                card+=str(create_even('N'))"""
        
    #one rule is even       
        if rule1=='even' or rule2=='even':
            #second is odd
            if rule2=='odd' or rule2=='odd':
               continue
            #second is royal
            elif rule2=='royal' or rule2=='royal':
                card+=str(create_even('Y'))
            #second is either one of the 4 suits or R/B
            else:
                card+=str(create_even('N'))
                
    #one rule is odd
        if rule1=='odd' or rule2=='odd':
            #second is even
            if rule2=='even' or rule2=='even':
               continue
            #second is royal
            elif rule2=='royal' or rule2=='royal':
                card+=str(create_odd('Y'))
            #second is either one of the 4 suits or R/B
            else:
                card+=str(create_odd('N'))
                
    #one rule is royal
        if rule1=='royal' or rule2=='royal':
            card+=create_royal()
            
    #one rule is diamond
        if rule1=='D' or rule2=='D':
            #second is black
            if rule1=='B' or rule2=='B':
                continue
            #second is hearts
            elif rule1=='H' or rule2=='H':
                print "here"
                continue
            #second is spade
            elif rule1=='S' or rule2=='S':
                continue
            #second is club
            elif rule1=='C' or rule2=='C':
                continue
            #second is red
            elif rule1=='R' or rule2=='R':
                card=card+str(random.randint(1,11))+'D'
                return card
            #second is either even,odd or royal
            elif rule1=='even' or rule2=='even' or rule1=='odd' or rule2=='odd' or rule1=='royal' or rule2=='royal':
                card+='D'
                return card


    #one rule is heart
        if rule1=='H' or rule2=='H':
            #second is black
            if rule1=='B' or rule2=='B':
                continue
            elif rule1=='D' or rule2=='D':
                continue
            elif rule1=='S' or rule2=='S':
                continue
            elif rule1=='C' or rule2=='C':
                continue
            elif rule1=='R' or rule2=='R':
                card=card+str(random.randint(1,11))+'H'
                return card
            elif rule1=='even' or rule2=='even' or rule1=='odd' or rule2=='odd' or rule1=='royal' or rule2=='royal':
                card+='H'
                return card

    #one rule is spade
        if rule1=='S' or rule2=='S':
           #second is red
            if rule1=='R' or rule2=='R':
                continue
            #second is diamond
            elif rule1=='D' or rule2=='D':
                continue
            #second is clubs
            elif rule1=='C' or rule2=='C':
                continue
            #second is hearts
            elif rule1=='H' or rule2=='H':
                continue
            #second is black
            elif rule1=='B' or rule2=='B':
                card=card+str(random.randint(1,11))+'S'
                return card
            #second is either even,odd or royal
            elif rule1=='even' or rule2=='even' or rule1=='odd' or rule2=='odd' or rule1=='royal' or rule2=='royal':
                card+='S'
                return card

    #one rule is club
        if rule1=='C' or rule2=='C':
            #second is red
            if rule1=='R' or rule2=='R':
                continue
            #second is diamond
            elif rule1=='D' or rule2=='D':
                continue
            #second is spade
            elif rule1=='S' or rule2=='S':
                continue
            #second is hearts
            elif rule1=='H' or rule2=='H':
                continue
            #second is black
            elif rule1=='B' or rule2=='B':
                card=card+str(random.randint(1,11))+'C'
                return card
            #second is either even,odd or royal
            elif rule1=='even' or rule2=='even' or rule1=='odd' or rule2=='odd' or rule1=='royal' or rule2=='royal':
                card+='C'
                return card
            """#second is even
            elif rule1=='even' or rule2=='even':
                card=card+str(create_even('N'))+'C'
                return card
            #second is odd
            elif rule1=='odd' or rule2=='odd':
                card=card+str(create_odd('N'))+'C'
                return card
            #second is royal
            elif rule1=='royal' or rule2=='royal':
                card=card+str(create_royal())+'C'
                return card"""

            
    #one rule is red
        if rule1=='R' or rule2=='R':
            #other one is black
            if rule1=='B' or rule2=='B':
                #for the case when one rule is red and other is black
                continue
            else:
                #for the case when any one of them is red
                card+=create_red()
                return card

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
