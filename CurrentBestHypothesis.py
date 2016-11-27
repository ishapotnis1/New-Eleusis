
from new_eleusis import *
from scientist import *
from card_generator import *



constraints={}
currentBestHypothesis={}
forvalidation={}
threshold=0.0
count=1


def current_best_hypothesis(hypothesis):
  temp={}
  tempconstraints={}
  tempValidation={}
  for (x,y) in hypothesis:
   for a in y:

    if  hypothesis[x][a]>0.005:
     temp[y]=hypothesis[x][a]


    if hypothesis[x][a]<0.001:
      tempconstraints[y] =hypothesis[x][a]


    else:
      tempValidation[y]=hypothesis[x][a]
   currentBestHypothesis[x]=temp
   constraints[x]=tempconstraints
   forvalidation[x]=tempValidation

   return currentBestHypothesis


def main():
 for i in range(1,200):
    previous2 = extraction(l[0])
    previous1 = extraction(l[1])
    current = extraction(l[2])
    comparison = comparator(previous2, previous1, current)
    p = probability(previous2, previous1, current, comparison)
    # print "for first three cards"
    # print comparison
    # print p
    count=i
    card = card_generator()
    print card + '\n'
    correct_wrong(card)
    card1 = extraction(card)
    previous2 = previous1
    previous1 = current
    current = card1
    comparison1 = comparator(previous2, previous1, current)
    p1 = probability(previous2, previous1, current, comparison)
    a1 = alternate(previous2, previous1, current, comparison)
    current_best_hypothesis(p1)

    print "for next card" + '\n'
    print comparison1
    print p1
    print a1


 if __name__ == "__main__":
    main()













