constraints=[];
currentBestHypothesis=[]



def card_generator():
 card='5H'
 return card

def check_for_thresh_hold(hypothesis):
 return True

def card_test(card):
 return True




def update_constraints(hypothesis):
 if check_for_thresh_hold(hypothesis)== False:
  constraints.append(hypothesis)

 else:
  rule_selector(hypothesis);


def rule_selector(hypothesis):
 #logic for current best hypothesis
