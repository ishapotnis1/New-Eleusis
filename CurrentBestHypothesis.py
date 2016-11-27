
from new_eleusis import *
from scientist import *
from card_generator import *



constraints={}
currentBestHypothesis={}
forvalidation={}
threshold=0.0
count=1


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

   print "THIS" ,currentBestHypothesis




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

    card = card_generator()

    correct_wrong(card)
    card1 = extraction(card)
    previous2 = previous1
    previous1 = current
    current = card1
    comparison1 = comparator(previous2, previous1, current)
    p1 = probability(previous2, previous1, current, comparison)
    a1 = alternate(previous2, previous1, current, comparison)

    current_best_hypothesis(p1)
#    alternate(a1)

    print "for next card " + '\n'
    print comparison1
    print p1
    print "ALTERNATE" ,a1


if __name__ == "__main__":
 main()











