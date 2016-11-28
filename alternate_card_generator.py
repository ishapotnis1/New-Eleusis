import random
from new_eleusis import *
import scientist
def alternateCard(alt):
    sampling = random.sample(alt,len(alt))
    rule1 =  random.choice(sampling)
    samplingNext = random.sample(alt[rule1],len(alt[rule1]))
    rule2 =  random.choice(samplingNext)
    print rule1 + " and " + rule2 
    if scientist.correct[rule1] == 1:
        if rule2 == "H" or rule2 == "S" or rule2 == "D" or rule2 == "C":
            number = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
            card = random.choice(number) + rule2
            print card
        if rule2 == 'even':
            number = ["2","4","6","8","10"]
            suit = ["H","S","D","C"]
            card = random.choice(number) + random.choice(suit)
            print card
        if rule2 == 'odd':
            number = ["A","3","5","7","9"]
            suit = ["H","S","D","C"]
            card = random.choice(number) + random.choice(suit)
            print card
        if rule2 == 'B':
            number = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
            suit = ["S","C"]
            card = random.choice(number) + random.choice(suit)
            print card
        if rule2 == 'R':
            number = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
            suit = ["H","D"]
            card = random.choice(number) + random.choice(suit)
            print card
        if rule2 == 'royal':
            number = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
            suit = ["S","C","H","D"]
            card = random.choice(number) + random.choice(suit)
            print card
    else:
        if rule1 == "H" or rule1 == "S" or rule1 == "D" or rule1 == "C":
            number = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
            card = random.choice(number) + rule1
            print card
        if rule1 == 'even':
            number = ["2","4","6","8","10"]
            suit = ["H","S","D","C"]
            card = random.choice(number) + random.choice(suit)
            print card
        if rule1 == 'odd':
            number = ["A","3","5","7","9"]
            suit = ["H","S","D","C"]
            card = random.choice(number) + random.choice(suit)
            print card
        if rule1 == 'B':
            number = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
            suit = ["S","C"]
            card = random.choice(number) + random.choice(suit)
            print card
        if rule1 == 'R':
            number = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
            suit = ["H","D"]
            card = random.choice(number) + random.choice(suit)
            print card
        if rule1 == 'royal':
            number = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
            suit = ["S","C","H","D"]
            card = random.choice(number) + random.choice(suit)
            print card
    return card
