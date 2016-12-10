from new_eleusis import *;
            
def perform():
    cards=['4H','2H','2D']
    #rule= If (equal(suit(current), suit(prev)), greater(value(current), value(prev)), True)
    prev2=cards[0]
    prev1=cards[1]
    current=cards[2]
    list=[]
    str1="or("
    #all even
    if even(prev2)==True and even(prev1)==True and even(current)==True:
        #all are even
        print "all even"
        list.append("even(current)")
        
    #all are odd
    if odd(prev2)==True and odd(prev1)==True and odd(current)==True:
        #all are odd
        print "all odd"
        list.append("odd(current)")
        
    #all are royal
    if is_royal(prev2)==True and is_royal(prev1)==True and is_royal(current)==True:
        #all are royal
        print "all royal"
        list.append("is_royal(current)")
        
    #all have same color
    if equal(color(prev2),color(prev1)) and equal(color(prev1),color(current)):
        #all are red
        print "all same color"
        if equal(color(prev2),'R')==True:
            print "all red"
            list.append("equal(color(current),'R')")
        else:
            print "all black"
            list.append("equal(color(current),'B')")
    
    #all belong to the same suit
    if equal(suit(prev2),suit(prev1)) and equal(suit(prev1),suit(current)):
        print "same suit"
        if equal(suit(current),'C'):
            print "all clubs"
            list.append("equal(suit(current),'C')")
        elif equal(suit(current),'H'):
            print "all hearts"
            list.append("equal(suit(current),'H')")
        elif equal(suit(current),'S'):
            print "all spades"
            list.append("equal(suit(current),'S')")

        else:
            print "all diamonds"
            list.append("equal(suit(current),'D')")
        
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

    for i in list:
        str1+=i+","
    str1=str1[:len(str1)-1]
    str1+=")"
    print str1
        
perform()

