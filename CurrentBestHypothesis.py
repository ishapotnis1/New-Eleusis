constraints=[]
currentBestHypothesis=[]
forvalidation=[]

def probability(x):
  return x;


'''
This function returns the list of rules which have to be tested. 
'''
def validator(x):
 forvalidation.append(x)
 return list

def check_for_upper_threshold(x):
 if probability(x) > 0.5:
  return True
 else:
   return False

def check_for_lower_threshhold(x):
 if probability(x) < 0.2:
  return True
 else:
  return False

def current_best_hypothesis(hypothesis):
  for x in hypothesis:
   if check_for_upper_threshold(x):
    currentBestHypothesis.append(hypothesis)

   if check_for_lower_threshhold(x):
     constraints.append(x)

   else:
     validator(x)

   return currentBestHypothesis

