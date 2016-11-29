import itertools,random
import scientist
import new_eleusis
#avg={}#'D':0.4,'royal':0.3,'even':0.33,'less':0.44}
#high={'H':0.55,'R':0.5,'odd':0.6,'plus1':0.56}
visited_rules=[]
#correct=['4H','2D','6H']
def number_to_value(number):
    """Given the numeric value of a card, returns its "value" name"""
    values = [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return values[int(number)]

def value_to_number(name):
    """Given the "value" part of a card, returns its numeric value"""
    values = [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    if name=='1':
        return values.index('A')
    else:
        return values.index(str(name))

#return less
def create_less(num,even):
    less=[]
    for i in range(1,value_to_number(num)):
        #if it is even then generate an even number less than the previously correct number
        if even=='Y':
            if i%2==0:
                less.append(i)
        #if it is odd then generate an odd number less than the previously correct number
        elif even=='N':
            if i%2!=0:
                less.append(i)
        #if it is royal then generate a royal number less than the previously correct number
        elif even=='R':
            if i<value_to_number(num) and i>11:
                less.append(i)
        #any number less than the previously correct number
        else:
            less.append(i)
    if len(less)>0:
	print less
        return number_to_value(random.choice(less))
    else:
        return ""

#return greater
def create_greater(num,even):
    greater=[]
    print "gr",num
    for i in range(value_to_number(num),14):
        #if it is even then generate an even number greater than the previously correct number
        if even=='Y':
            if i%2==0:
                greater.append(i)
        #if it is odd then generate an odd number greater than the previously correct number
        elif even=='N':
            if i%2!=0:
                greater.append(i)
        #if it is royal then generate a royal number greater than the previously correct number
        elif even=='R':
            if i>value_to_number(num):
                greater.append(i)
        #any number greater than the previous correct number
        else:
            greater.append(i)
    if len(greater)>0:
	print greater
        return number_to_value(random.choice(greater))
    else:
        return ""

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
def create_red(avg,high):
    probD=0.0
    probH=0.0
    if len(avg)!=0 or len(high)!=0:
        if 'D' in avg:
            probD=avg['D']
        if 'H' in avg:
            probH=avg['H']
        if len(high)!=0:
            if 'D' in high:
                probD=high['D']
            if 'H' in high:
                probH=high['H']
            if probD>probH:
                return 'D'
            else:
                return 'H'
    
#return spade or club if rule is black based on their probabilities      
def create_black(avg,high):
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

#manipulation on rules selected
def check(rule1,rule2,avg,high,last_correct):
    card=""
    #one rule is even       
    if rule1=='even' or rule2=='even':
        #second is odd DISCARD
        if rule1=='odd' or rule2=='odd':
            return ""
        #second is royal
        elif rule1=='royal' or rule2=='royal':
            card+=str(create_even('Y'))+create_suit()
            return card
        #second is minus1 of the previously correct card DISCARD
        elif rule1=='minus1' or rule2=='minus1':
            return ""
        #second is plus1 of the previously correct card DISCARD
        elif rule1=='plus1' or rule2=='plus1':
            return ""
        #second is less than the previously correct card by any amount
        elif rule1=='less' or rule2=='less':
            if len(last_correct)!=0:
				x=create_less(last_correct[0],'Y')
				if x!="":
					card+=x+create_suit()
					return card
				else:
					return ""
            else:
                return ""
        #second is greater than the previously correct card by any amount
        elif rule1=='greater' or rule2=='greater':
            if len(last_correct)!=0:
				x=create_greater(last_correct[0],'Y')
				if x!="":
					card+=x+create_suit()
					return card
				else:
					return ""
            else:
                return ""
        #second is either one of the 4 suits or R/B
        else:
            card+=str(create_even('N'))
                
    #one rule is odd
    if rule1=='odd' or rule2=='odd':
        #second is even DISCARD
        if rule1=='even' or rule2=='even':
             return ""
        #second is royal
        elif rule1=='royal' or rule2=='royal':
            print "why yar"
            card+=str(create_odd('Y'))+create_suit()
            return card
        #second is minus1 of the previously correct card DISCARD
        elif rule1=='minus1' or rule2=='minus1':
            return ""
        #second is plus1 of the previously correct card DISCARD
        elif rule1=='plus1' or rule2=='plus1':
            return ""
        #second is less than the previously correct card by any amount
        elif rule1=='less' or rule2=='less':
            if len(last_correct)!=0:
				x=create_less(last_correct[0],'N')
				if x!="":
					card+=x+create_suit()
					return card
				else:
					return ""
            else:
                return ""
        #second is greater than the previously correct card by any amount
        elif rule1=='greater' or rule2=='greater':
            if len(last_correct)!=0:
				x=create_greater(last_correct[0],'N')
				if x!="":
					card+=x+create_suit()
					return card
				else:
					return ""
            else:
                return ""
        #second is either one of the 4 suits or R/B
        else:
            card+=str(create_odd('N'))
                
    #one rule is royal
    if rule1!='even' or rule1!='odd' or rule2!='even' or rule2!='odd':
        if rule1=='royal' or rule2=='royal':
            #second is less than the previous correct card
            if rule1=='less' or rule2=='less':
                if len(last_correct)!=0:
					x=create_less(last_correct[0],'R')
					if x!="":
						card+=x+create_suit()
						return card
					else:
						return ""
                else:
                    return ""
            #second is greater than the previous correct card
            elif rule1=='greater' or rule2=='greater':
                if len(last_correct)!=0:
					x=create_greater(last_correct[0],'R')
					print x
					if x!=0:
						card+=x+create_suit()
						return card
					else:
						return ""
                else:
                    return ""
            #second is one greater than the previous correct card
            elif rule1=='plus1' or rule2=='plus1':
                if len(last_correct)!=0:
                    print value_to_number(last_correct[0])+1
                    if (value_to_number(last_correct[0])+1)<14:
                        card+=number_to_value(value_to_number(last_correct[0])+1)+create_suit()
                        return card
                    else:
                        return ""
                else:
                    return ""
            #second is one less than the previous correct card
            elif rule1=='minus1' or rule2=='minus1':
                if len(last_correct)!=0:
                    print value_to_number(last_correct[0])-1
                    if (value_to_number(last_correct[0])-1)>10:
                        card+=number_to_value(value_to_number(last_correct[0])-1)+create_suit()
                        return card
                    else:
                        return ""
                else:
                    return ""
            else:
                card+=create_royal()

        
    #one rule is diamond
    if rule1=='D' or rule2=='D':
        #second is black DISCARD
        if rule1=='B' or rule2=='B':
            return ""
        #second is hearts DISCARD
        elif rule1=='H' or rule2=='H':
            print "here"
            return ""
        #second is spade DISCARD
        elif rule1=='S' or rule2=='S':
            return ""
        #second is club DISCARD
        elif rule1=='C' or rule2=='C':
            return ""
        #second is red
        elif rule1=='R' or rule2=='R':
            card=card+number_to_value(random.randint(1,11))+'D'
            return card
        #second is either even,odd or royal
        elif rule1=='even' or rule2=='even' or rule1=='odd' or rule2=='odd' or rule1=='royal' or rule2=='royal':
            print "why not"
            card+='D'
            return card
        #second is less than the previous correct card
        elif rule1=='less' or rule2=='less':
            if len(last_correct)!=0:
				x=create_less(last_correct[0],'E')
				if x!="":
					card+=x+'D'
					return card
				else:
					return ""
            else:
                return ""
        #second is greater than the previous correct card
        elif rule1=='greater' or rule2=='greater':
            if len(last_correct)!=0:
				x=create_greater(last_correct[0],'E')
				if x!=0:
					card+=x+'D'
					return card
				else:
					return ""
            else:
                return ""
        #second is one greater than the previous correct card
        elif rule1=='plus1' or rule2=='plus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])+1)<14:
                    card+=number_to_value(value_to_number(last_correct[0])+1)+'D'
                    return card
                else:
                    return ""
            else:
                return ""
        #second is one less than the previous correct card
        elif rule1=='minus1' or rule2=='minus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])-1)>0:
                    card+=number_to_value(value_to_number(last_correct[0])-1)+'D'
                    return card
                else:
                    return ""
            else:
                return ""


    #one rule is heart
    if rule1=='H' or rule2=='H':
        #second is black DISCARD
        if rule1=='B' or rule2=='B':
            return ""
        #second is spade DISCARD
        elif rule1=='S' or rule2=='S':
            return ""
        #second is club DISCARD
        elif rule1=='C' or rule2=='C':
            return ""
        elif rule1=='R' or rule2=='R':
            card=card+number_to_value(random.randint(1,11))+'H'
            return card
        elif rule1=='even' or rule2=='even' or rule1=='odd' or rule2=='odd' or rule1=='royal' or rule2=='royal':
            card+='H'
            return card
        #second is less than the previous correct card
        elif rule1=='less' or rule2=='less':
            if len(last_correct)!=0:
				x=create_less(last_correct[0],'E')
				if x!="":
					card+=x+'H'
					return card
				else:
					return ""
            else:
                return ""
        #second is greater than the previous correct card
        elif rule1=='greater' or rule2=='greater':
            if len(last_correct)!=0:
				x=create_greater(last_correct[0],'E')
				if x!="":
					card+=x+'H'
					return card
				else:
					return ""
            else:
                return ""
        #second is one greater than the previous correct card
        elif rule1=='plus1' or rule2=='plus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])+1)<14:
                    card+=number_to_value(value_to_number(last_correct[0])+1)+'H'
                    return card
                else:
                    return ""
            else:
                return ""
        #second is one less than the previous correct card
        elif rule1=='minus1' or rule2=='minus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])-1)>0:
                    card+=number_to_value(value_to_number(last_correct[0])-1)+'H'
                    return card
                else:
                    return ""
            else:
                return ""

    #one rule is spade
    if rule1=='S' or rule2=='S':
         #second is red DISCARD
        if rule1=='R' or rule2=='R':
            return ""
        #second is clubs DISCARD
        elif rule1=='C' or rule2=='C':
            return ""
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
            if len(last_correct)!=0:
				x=create_less(last_correct[0],'E')
				if x!="":
					card+=x+'S'
					return card
				else:
					return ""
            else:
                return ""
        #second is greater than the previous correct card
        elif rule1=='greater' or rule2=='greater':
            if len(last_correct)!=0:
				x=create_greater(last_correct[0],'E')
				if x!="":
					card+=x+'S'
					return card
				else:
					return ""
            else:
                return ""
        #second is one greater than the previous correct card
        elif rule1=='plus1' or rule2=='plus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])+1)<14:
                    card+=number_to_value(value_to_number(last_correct[0])+1)+'S'
                    return card
                else:
                    return ""
            else:
                return ""
        #second is one less than the previous correct card
        elif rule1=='minus1' or rule2=='minus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])-1)>0:
                    card+=number_to_value(value_to_number(last_correct[0])-1)+'S'
                    return card
                else:
                    return ""
            else:
                return ""
            
    #one rule is club
    if rule1=='C' or rule2=='C':
        #second is red DISCARD
        if rule1=='R' or rule2=='R':
            return ""
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
            if len(last_correct)!=0:
				x=create_less(last_correct[0],'E')
				if x!="":
					card+=x+'C'
					return card
				else:
					return ""
            else:
                return ""
        #second is greater than the previous correct card
        elif rule1=='greater' or rule2=='greater':
            if len(last_correct)!=0:
				x=create_greater(last_correct[0],'E')
				if x!="":
					card+=x+'C'
					return card
				else:
					return ""
            else:
                return ""
        #second is one greater than the previous correct card
        elif rule1=='plus1' or rule2=='plus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])+1)<14:
                    card+=number_to_value(value_to_number(last_correct[0])+1)+'C'
                    return card
                else:
                    return ""
            else:
                return ""
        #second is one less than the previous correct card
        elif rule1=='minus1' or rule2=='minus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])-1)>0:
                    card+=number_to_value(value_to_number(last_correct[0])-1)+'C'
                    return card
                else:
                    return ""
            else:
                return ""
        
    #one rule is red
    if rule1=='R' or rule2=='R':
        #other one is black
        if rule1=='B' or rule2=='B':
            #for the case when one rule is red and other is black DISCARD
            return ""
        #when second card is less than the previous correct card
        elif rule1=='less' or rule2=='less':
            if len(last_correct)!=0:
				x=create_less(last_correct[0],'E')
				if x!="":
					card+=x+create_red(avg,high)
					return card
				else:
					return ""
            else:
                return ""
        #when second card is greater than the previous correct card
        elif rule1=='greater' or rule2=='greater':
            if len(last_correct)!=0:
				x=create_greater(last_correct[0],'E')
				if x!="":
					card+=x+create_red(avg,high)
					return card
				else:
					return ""
            else:
                return ""
        #when second card is one greater than the previous correct card
        elif rule1=='plus1' or rule2=='plus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])+1)<14:
                    card+=number_to_value(value_to_number(last_correct[0])+1)+create_red(avg,high)
                    return card
                else:
                    return ""
            else:
                return ""
        #when second card is one less than the previous correct card
        elif rule1=='minus1' or rule2=='minus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])-1)>0:
                    card+=number_to_value(value_to_number(last_correct[0])-1)+create_red(avg,high)
                    return card
                else:
                    return ""
            else:
                return ""
        else:
            #for the case when any one of them is red
            card+=create_red(avg,high)
            return card

    #one rule is black
    if rule1=='B' or rule2=='B':
        #when second card is less than the previous correct card
        if rule1=='less' or rule2=='less':
            if len(last_correct)!=0:
				x=create_less(last_correct[0],'E')
				if x!="":
					card+=x+create_black(avg,high)
					return card
				else:
					return ""
            else:
                return ""
        #when second card is greater than the previous correct card
        elif rule1=='greater' or rule2=='greater':
            if len(last_correct)!=0:
				x=create_greater(last_correct[0],'E')
				if x!="":
					card+=x+create_black(avg,high)
					return card
				else:
					return ""
            else:
                return ""
        #when second card is one greater than the previous correct card
        elif rule1=='plus1' or rule2=='plus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])+1)<14:
                    card+=number_to_value(value_to_number(last_correct[0])+1)+create_black(avg,high)
                    return card
                else:
                    return ""
            else:
                return ""
        #when second card is one less than the previous correct card
        elif rule1=='minus1' or rule2=='minus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])-1)>0:
                    card+=number_to_value(value_to_number(last_correct[0])-1)+create_black(avg,high)
                    return card
                else:
                    return ""
            else:
                return ""
        else:
            #case when one of them is black
            card+=create_black(avg,high)
            return card
            
    #one is less than the previous correct card     
    if rule1=='less' or rule2=='less':
        #second is one greater than the previous DISCARD
        if rule1=='plus1' or rule2=='plus1':
            return ""
        #second is greater DISCARD
        elif rule1=='greater' or rule2=='greater':
            return ""
        #second is one less than the previous correct card
        elif rule1=='minus1' or rule2=='minus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])-1)>0:
                    card+=number_to_value(value_to_number(last_correct[0])-1)+create_suit()
                    return card
                else:
                    return ""
            else:
                return ""
                            
    #one is one less than the previous correct card         
    if rule1=='minus1' or rule2=='minus1':
        #second is one greater DISCARD
        if rule1=='plus1' or rule2=='plus1':
            return ""
        #second is greater DISCARD
        elif rule1=='greater' or rule2=='greater':
            return ""
            
    #one is greater than the previous correct card          
    if rule1=='greater' or rule2=='greater':
        #second is one greater than the previous correct so this dominates
        if rule1=='plus1' or rule2=='plus1':
            if len(last_correct)!=0:
                if (value_to_number(last_correct[0])+1)<14:
                    card+=number_to_value(value_to_number(last_correct[0])+1)+create_suit()
                    return card
                else:
                    return ""
            else:
                return ""
   

#generate the new card   
def card_generator(avg,high,correct):
    print "in card generator"
    last_correct=""
    if len(correct)!=0:
        last_correct=correct[len(correct)-1]
    print "last_correct",last_correct
    count=0
    #to keep a count of how many cards have been generated
    count+=1
    if len(avg)!=0 and len(high)!=0:
        perm = list(itertools.product(avg.keys(), high.keys()))
        random.shuffle(perm)
        
        for i in perm:
            card=""
            #separating rules from generated permutation
            rule1,rule2=i
            print rule1,rule2
            card=check(rule1,rule2,avg,high,last_correct)
            if card=="":
                continue
            else:
                return card

    #avg list is empty            
    elif len(avg)==0:
        print high
        for i in high.keys():
            #generate combinations using high list only
            highcombo = list(itertools.product(high.keys(),repeat=2))
            random.shuffle(highcombo)
        
            for i in highcombo:
                print i
                card=""
                #separating rules from generated permutation
                rule1,rule2=i
                print rule1,rule2
                if rule1==rule2:
                    continue
                else:
                    card=check(rule1,rule2,avg,high,last_correct)
                if card=="":
                    continue
                else:
                    return card
                
    elif len(high)==0:
        print "avg",avg
        for i in avg.keys():
            avgcombo = list(itertools.combinations(avg.keys(),repeat=2))
            random.shuffle(avgcombo)
     
            for i in avgcombo:
                print i
                card=""
                #separating rules from generated permutation
                rule1,rule2=i
                print rule1,rule2
                if rule1==rule2:
                    continue
                else:
                    card=check(rule1,rule2,avg,high,last_correct)
                if card=="":
                    continue
                else:
                    return card
                
def random_card():
    card=""
    card+=number_to_value(random.randint(1,11))+create_suit()
    print card
    return card
