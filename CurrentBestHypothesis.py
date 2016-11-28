
from new_eleusis import *
from scientist import *
from card_generator import *

count=1

cb={}

constraints={}
currentBestHypothesis={}
forvalidation={}
threshold=0.0
hypothesisforgeneration={}
temp={}


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
  for a,x in possible_values.iteritems():
   if x>0.005:
    temp[a]=x
    hypothesisforgeneration[a]=x
   if x<0.002:
    tempconstraints[a]=x

   if x>0.002 and x<0.005:
    tempValidation[a]=x
    forvalidation[a] = x
   currentBestHypothesis[field] = temp
   constraints[field] = tempconstraints





  print "SRISHTY",currentBestHypothesis
  print "NITIKA", hypothesisforgeneration

  return hypothesisforgeneration


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
    card = '4H'

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











