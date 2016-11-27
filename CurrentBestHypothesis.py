
from new_eleusis import *
from scientist import *
from card_generator import *

count=0

cb={}

constraints={}
currentBestHypothesis={}
forvalidation={}
threshold=0.0



"""def alternate(a1t):
 for field, possible_values in hypothesis.iteritems():
  print  field, possible_values
   for a, x in possible_values.iteritems():"""




def validator():
 return forvalidation




def current_best_hypothesis(hypothesis):
  temp={}
  tempconstraints={}
  tempValidation={}


  for field, possible_values in hypothesis.iteritems():
   print  field , possible_values
   for a,x in possible_values.iteritems():
    if x>0.005:
     temp[a]=x
    if x<0.002:
     tempconstraints[a]=x
    else:
      tempValidation[a]=x
    currentBestHypothesis[field] = temp
    constraints[field] = tempconstraints
    forvalidation[field] = tempValidation




  print "this is",currentBestHypothesis

  return currentBestHypothesis


def main():
  for i in range(1,100):
    previous2 = extraction(l[0])
    previous1 = extraction(l[1])
    current = extraction(l[2])
    comparison = comparator(previous2, previous1, current)
    p = probability(previous2, previous1, current, comparison)
    # print "for first three cards"
    # print comparison
    # print p
    print "hvnbvnbv", currentBestHypothesis
    card = card_generator()

    correct_wrong(card)
    card1 = extraction(card)
    previous2 = previous1
    previous1 = current
    current = card1
    comparison1 = comparator(previous2, previous1, current)
    p1 = probability(previous2, previous1, current, comparison)
    a1 = alternate(previous2, previous1, current, comparison)

    cb=current_best_hypothesis(p1)
    print "count" ,CurrentBestHypothesis.count
    if CurrentBestHypothesis.count==3:

     for field, possible_values in  currentBestHypothesis.iteritems():
      for a, x in possible_values.iteritems():
       print field, a





if __name__ == "__main__":
 main()











