from new_eleusis import *
from scientist import *

count=0

cb={}

constraints={}
currentBestHypothesis={}
forvalidation={}
threshold=0.0




def current_best_hypothesis(hypothesis):
temp={}
tempconstraints={}
tempValidation={}


for field, possible_values in hypothesis.iteritems():
print  field , possible_values
for a,x in possible_values.iteritems():
if x>0.005:
currentBestHypothesis[a] = x
if x<0.002:
constraints[a] = x
if x<0.005 and x>0.002:
forvalidation[a] = x

print "thisis",currentBestHypothesis
return forvalidation,currentBestHypothesis
