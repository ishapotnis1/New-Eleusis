import random
from new_eleusis import *
from scientist import *
from card_generator import *

l=['6S','7D','8S']

def alternateCard(correct):
    previous2 = scientist.extraction(correct[len(correct) - 3])
    previous1 = scientist.extraction(correct[len(correct) - 2])
    current = scientist.extraction(correct[len(correct) - 1])
   
    comparison = scientist.comparator(previous2, previous1, current)
    alt = scientist.alternate(previous2, previous1, current)
   
    sampling = random.sample(alt,len(alt))
    rule1 =  random.choice(sampling)
    samplingNext = random.sample(alt[rule1],len(alt[rule1]))
    rule2 =  random.choice(samplingNext)
   
    if current[rule1] == 1:
        if rule2 == "H" or rule2 == "S" or rule2 == "D" or rule2 == "C":
            number = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
            card = random.choice(number) + rule2
            
        if rule2 == 'even':
            number = ["2","4","6","8","10"]
            suit = ["H","S","D","C"]
            card = random.choice(number) + random.choice(suit)
            
        if rule2 == 'odd':
            number = ["A","3","5","7","9"]
            suit = ["H","S","D","C"]
            card = random.choice(number) + random.choice(suit)
            
        if rule2 == 'B':
            number = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
            suit = ["S","C"]
            card = random.choice(number) + random.choice(suit)
            
        if rule2 == 'R':
            number = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
            suit = ["H","D"]
            card = random.choice(number) + random.choice(suit)
            
        if rule2 == 'royal':
            number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
            suit = ["S","C","H","D"]
            card = random.choice(number) + random.choice(suit)
            
    else:
        if rule1 == "H" or rule1 == "S" or rule1 == "D" or rule1 == "C":
            number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
            card = random.choice(number) + rule1
            
        if rule1 == 'even':
            number = ["2","4","6","8","10"]
            suit = ["H","S","D","C"]
            card = random.choice(number) + random.choice(suit)
            
        if rule1 == 'odd':
            number = ["A","3","5","7","9"]
            suit = ["H","S","D","C"]
            card = random.choice(number) + random.choice(suit)
            
        if rule1 == 'B':
            number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
            suit = ["S","C"]
            card = random.choice(number) + random.choice(suit)
            print card
        if rule1 == 'R':
            number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
            suit = ["H","D"]
            card = random.choice(number) + random.choice(suit)
            print card
        if rule1 == 'royal':
            number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
            suit = ["S","C","H","D"]
            card = random.choice(number) + random.choice(suit)
            print card
    return card
