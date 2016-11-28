import itertools,random
import scientist
import new_eleusis
avg={'D':0.4,'royal':0.3,'even':0.33,'less':0.44}
high={'H':0.55,'R':0.5,'odd':0.6,'plus1':0.56}
visited_rules=[]
correct=['4H','2D','6H']

def number_to_value(number):
    """Given the numeric value of a card, returns its "value" name"""
    values = [None, 'A', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'J', 'Q', 'K']
    return values[number]

def value_to_number(name):
    """Given the "value" part of a card, returns its numeric value"""
    values = [None, 'A', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'J', 'Q', 'K']
    return values.index(name)

#return less
def create_less(num,even):
    less=[]
    for i in range(1,value_to_number(num)):
        #if it is even then generate an even number greater than the previously correct number
        if even=='Y':
            if i%2==0:
                less.append(i)
        #if it is odd then generate an odd number greater than the previously correct number
        elif even=='N':
            if i%2!=0:
                less.append(i)
        elif even=='R':
            if i<value_to_number(num) and i>11:
                less.append(i)
        else:
            less.append(i)
    return number_to_value(random.choice(less))

#return greater
def create_greater(num,even):
    greater=[]
    for i in range(value_to_number(num),14):
        #if it is even then generate an even number greater than the previously correct number
        if even=='Y':
            if i%2==0:
                greater.append(i)
        #if it is odd then generate an odd number greater than the previously correct number
        elif even=='N':
            if i%2!=0:
                greater.append(i)
        elif even=='R':
            if i>value_to_number(num):
                greater.append(i)
        else:
            less.append(i)
    return number_to_value(random.choice(greater))

#return a royal 
def create_royal():
    royal=['J','Q','K']
    return random.choice(royal)

#return a suit 
def create_suit():
    suit=['D','H','C','S']
    return random.choice(suit)

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
        return number_to_value(random.choice(odd))
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
    last_correct=""
    last_correct=correct[len(correct)-1]
    print "last_correct",last_correct,last_correct[0]
    print "in card generator"
    print avg,"best",high
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
        print rule1,rule2
        visited_rules.append(rule1)
        visited_rules.append(rule2)
        
    #one rule is even       
        if rule1=='even' or rule2=='even':
            #second is odd
            if rule1=='odd' or rule2=='odd':
               continue
            #second is royal
            elif rule1=='royal' or rule2=='royal':
                card+=str(create_even('Y'))+create_suit()
                return card
            #second is minus1 of the previously correct card
            elif rule1=='minus1' or rule2=='minus1':
                print int(last_correct[0])-1
                if (int(last_correct[0])-1)>0:
                    card+=(number_to_value(int(last_correct[0])-1))+create_suit()
                    return card
            #second is plus1 of the previously correct card
            elif rule1=='plus1' or rule2=='plus1':
                if (int(last_correct[0])+1)<14:
                    print int(last_correct[0])+1
                    card+=(number_to_value(int(last_correct[0])+1))+create_suit()
                    return card
            #second is less than the previously correct card by any amount
            elif rule1=='less' or rule2=='less':
                card+=create_less(last_correct[0],'Y')+create_suit()
                return card
            #second is greater than the previously correct card by any amount
            elif rule1=='greater' or rule2=='greater':
                card+=create_greater(last_correct[0],'Y')+create_suit()
                return card
            #second is either one of the 4 suits or R/B
            else:
                card+=str(create_even('N'))
                
    #one rule is odd
        if rule1=='odd' or rule2=='odd':
            #second is even
            if rule1=='even' or rule2=='even':
               continue
            #second is royal
            elif rule1=='royal' or rule2=='royal':
                card+=str(create_odd('Y'))+create_suit()
                return card
            #second is minus1 of the previously correct card
            elif rule1=='minus1' or rule2=='minus1':
                print value_to_number(int(last_correct[0]))-1
                if (value_to_number(int(last_correct[0]))-1)>0:
                    card+=(value_to_number(int(last_correct[0])-1))+create_suit()
                    return card
                else:
                    continue
            #second is plus1 of the previously correct card
            elif rule1=='plus1' or rule2=='plus1':
                print value_to_number(int(last_correct[0]))+1
                if (value_to_number(int(last_correct[0]))+1)<14:
                    card+=(value_to_number(int(last_correct[0])+1))+create_suit()
                    return card
                else:
                    continue
            #second is less than the previously correct card by any amount
            elif rule1=='less' or rule2=='less':
                card+=create_less(value_to_number(last_correct[0]),'N')+create_suit()
                return card
            #second is greater than the previously correct card by any amount
            elif rule1=='greater' or rule2=='greater':
                card+=create_greater(value_to_number(last_correct[0]),'N')+create_suit()
                return card
            #second is either one of the 4 suits or R/B
            else:
                card+=str(create_odd('N'))
                
    #one rule is royal
        if rule1!='even' or rule1!='odd' or rule2!='even' or rule2!='odd':
            if rule1=='royal' or rule2=='royal':
                if rule1=='less' or rule2=='less':
                    card+=create_less(value_to_number(last_correct[0]),'R')
                elif rule1=='greater' or rule2=='greater':
                    card+=create_greater(value_to_number(last_correct[0]),'R')
                elif rule1=='plus1' or rule2=='plus1':
                    print int(last_correct[0])+1
                    if (value_to_number(last_correct[0]+1))<14:
                        card+=number_to_value((value_to_number(int(last_correct[0]))+1))
                    else:
                        continue
                elif rule1=='minus1' or rule2=='minus1':
                    print int(last_correct[0])-1
                    if (value_to_number(last_correct[0])-1)>10:
                        card+=number_to_value((value_to_number(int(last_correct[0]))-1))
                    else:
                        continue
                else:
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
                card=card+number_to_value(random.randint(1,11))+'D'
                return card
            #second is either even,odd or royal
            elif rule1=='even' or rule2=='even' or rule1=='odd' or rule2=='odd' or rule1=='royal' or rule2=='royal':
                card+='D'
                return card
            #second is less than the previous correct card
            elif rule1=='less' or rule2=='less':
                card+=create_less(last_correct[0],'E')+'D'
                return card
            #second is greater than the previous correct card
            elif rule1=='greater' or rule2=='greater':
                card+=create_greater(last_correct[0],'E')+'D'
                return card
            #second is one greater than the previous correct card
            elif rule1=='plus1' or rule2=='plus1':
                if (value_to_number(int(last_correct[0]))+1)<14:
                    card+=number_to_value(value_to_number(int(last_correct[0]))+1)+'D'
                    return card
                else:
                    continue
            #second is one less than the previous correct card
            elif rule1=='minus1' or rule2=='minus1':
                if (value_to_number(int(last_correct[0]))-1)>0:
                        card+=number_to_value(value_to_number(int(last_correct[0]))-1)+'D'
                        return card
                else:
                    continue


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
                card=card+number_to_value(random.randint(1,11))+'H'
                return card
            elif rule1=='even' or rule2=='even' or rule1=='odd' or rule2=='odd' or rule1=='royal' or rule2=='royal':
                card+='H'
                return card
            #second is less than the previous correct card
            elif rule1=='less' or rule2=='less':
                card+=create_less(last_correct[0],'E')+'H'
                return card
            #second is greater than the previous correct card
            elif rule1=='greater' or rule2=='greater':
                card+=create_greater(last_correct[0],'E')+'H'
                return card
            #second is one greater than the previous correct card
            elif rule1=='plus1' or rule2=='plus1':
                if (value_to_number(int(last_correct[0]))+1)<14:
                    card+=number_to_value(value_to_number(int(last_correct[0]))+1)+'H'
                    return card
                else:
                    continue
            #second is one less than the previous correct card
            elif rule1=='minus1' or rule2=='minus1':
                if (value_to_number(int(last_correct[0]))-1)>0:
                        card+=number_to_value(value_to_number(int(last_correct[0]))-1)+'H'
                        return card
                else:
                    continue

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
                card=card+number_to_value(random.randint(1,11))+'S'
                return card
            #second is either even,odd or royal
            elif rule1=='even' or rule2=='even' or rule1=='odd' or rule2=='odd' or rule1=='royal' or rule2=='royal':
                card+='S'
                return card
            #second is less than the previous correct card
            elif rule1=='less' or rule2=='less':
                card+=create_less(last_correct[0],'E')+'S'
                return card
            #second is greater than the previous correct card
            elif rule1=='greater' or rule2=='greater':
                card+=create_greater(last_correct[0],'E')+'S'
                return card
            #second is one greater than the previous correct card
            elif rule1=='plus1' or rule2=='plus1':
                if (value_to_number(int(last_correct[0]))+1)<14:
                    card+=number_to_value(value_to_number(int(last_correct[0]))+1)+'S'
                    return card
                else:
                    continue
            #second is one less than the previous correct card
            elif rule1=='minus1' or rule2=='minus1':
                if (value_to_number(int(last_correct[0]))-1)>0:
                        card+=number_to_value(value_to_number(int(last_correct[0]))-1)+'S'
                        return card
                else:
                    continue

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
                card=card+number_to_value(random.randint(1,11))+'C'
                return card
            #second is either even,odd or royal
            elif rule1=='even' or rule2=='even' or rule1=='odd' or rule2=='odd' or rule1=='royal' or rule2=='royal':
                card+='C'
                return card
            #second is less than the previous correct card
            elif rule1=='less' or rule2=='less':
                card+=create_less(last_correct[0],'E')+'C'
                return card
            #second is greater than the previous correct card
            elif rule1=='greater' or rule2=='greater':
                card+=create_greater(last_correct[0],'E')+'C'
                return card
            #second is one greater than the previous correct card
            elif rule1=='plus1' or rule2=='plus1':
                if (value_to_number(int(last_correct[0]))+1)<14:
                    card+=number_to_value(value_to_number(int(last_correct[0]))+1)+'C'
                    return card
                else:
                    continue
            #second is one less than the previous correct card
            elif rule1=='minus1' or rule2=='minus1':
                if (value_to_number(int(last_correct[0]))-1)>0:
                        card+=number_to_value(value_to_number(int(last_correct[0]))-1)+'C'
                        return card
                else:
                    continue
                

            
    #one rule is red
        if rule1=='R' or rule2=='R':
            #other one is black
            if rule1=='B' or rule2=='B':
                #for the case when one rule is red and other is black
                continue
            #when second card is less than the previous correct card
            elif rule1=='less' or rule2=='less':
                card+=create_less(last_correct[0],'E')
            #when second card is greater than the previous correct card
            elif rule1=='greater' or rule2=='greater':
                card+=create_greater(last_correct[0],'E')
            #when second card is one greater than the previous correct card
            elif rule1=='plus1' or rule2=='plus1':
                if (value_to_number(int(last_correct[0]))+1)<14:
                        card+=number_to_value(value_to_number(int(last_correct[0]))+1)+create_red()
                        return card
                else:
                    continue
            #when second card is one less than the previous correct card
            elif rule1=='minus1' or rule2=='minus1':
                if (value_to_number(int(last_correct[0]))-1)>0:
                        card+=number_to_value((value_to_number(int(last_correct[0]))-1))+create_red()
                        return card
                else:
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
            #when second card is less than the previous correct card
            elif rule1=='less' or rule2=='less':
                card+=create_less(last_correct[0],'E')
            #when second card is greater than the previous correct card
            elif rule1=='greater' or rule2=='greater':
                card+=create_greater(last_correct[0],'E')
            #when second card is one greater than the previous correct card
            elif rule1=='plus1' or rule2=='plus1':
                if (value_to_number(int(last_correct[0]))+1)<14:
                        card+=number_to_value(value_to_number(int(last_correct[0]))+1)+create_black()
                        return card
                else:
                    continue
            #when second card is one less than the previous correct card
            elif rule1=='minus1' or rule2=='minus1':
                if (value_to_number(int(last_correct[0]))-1)>0:
                        card+=number_to_value((value_to_number(int(last_correct[0]))-1))+create_black()
                        return card
                else:
                    continue
            else:
                #case when one of them is black
                card+=create_black()
                return card
print card_generator()
