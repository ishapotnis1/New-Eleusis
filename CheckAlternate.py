#  (is_royal(current), False)
import re


import pyparsing # make sure you have this installed

map={}
map['A']='1'
map['J']='11'
map['Q']='12'
map['K']='13'


def parseRule(rule):

 list2 = []
 list3 = []
 list4=[]
 list=rule.split("(")
 print list

 for x in list:
  list2=list2+x.split(")")
 #print list2
 for x in list2:
  list3=list3+x.split(",")
 for x in list3:
  if x=="":
   list3.remove(x)
 for x in list3:
  list4 = list4 + x.split(" ")
 for x in list4:
  if x=="":
   list4.remove(x)

 return list4


def breakrules(list):
 flag=0
 dictionaryofrules={}
 listTemp=[]
 rule=""
 result=""
 for x in list:
  if(x!=""):
   if x=="True" or x=="False":
    result=x
    break
   if x=="equal" or x=="greater" or x=="less":
    rule=x
    listTemp=[]




   else:
    listTemp.append(x)
    dictionaryofrules[rule]=listTemp

  return dictionaryofrules





def extract(attribute,card):
 color="M"
 suit="a"

 if len(card)<3:
  suit=card[1]
  if card[0]!='A' and card[0]!='J'and card[0]!='Q' and card[0]!='K':
   Value=card[0]
  else:
   Value=map[card[0]]
 else:
     Value=card[0]+card[1]
     suit=card[2]
 if suit=='D' or suit=='H':
  color='R'
 else:
  color='B'

 if attribute == "Value":
  return Value
 if attribute == "Color":
  return  color
 if attribute == "Suit":
  return suit

 return








def checkCard(card,list,hypothesis):


  allowedvalues=[]
  allowedsuits=[]
  even = ['2', '4', '6', '8', '10', 'Q']
  odd = ['A', '3', '5', '7', '9', 'J', 'K']
  if "even" in list:
   allowedvalues=['2','4','6','8','10','Q']

  if "odd" in list:
   allowedvalues = ['A', '3', '5', '7', '9', 'J','K']

  if "Royal" in list:
   allowedsuits=['A','Q','J','K']

  suitcurrent=extract("Suit",card)
  valuecurrent=extract("Value",card)
  colorcurrent = extract("Color", card)

  allowedsuits=list+allowedsuits
  allowedvalues=list+allowedvalues



  if suitcurrent in allowedsuits:
   hypothesis=hypothesis+ "AND "+"equal(suit(current),"+ ","+suitcurrent+"))"

  if valuecurrent in allowedvalues:
   x=""
   if valuecurrent in even:
    x="even"
   if valuecurrent in odd:
    x="odd"
   hypothesis = hypothesis + "AND "+  x

  if colorcurrent in list:
   hypothesis = hypothesis +"and "+ "equal(color(current),"+ ","+colorcurrent+"))"




  return hypothesis


def findSimilarity(card1,card2,list,hypothesis,correct):
    allowedvalues = []
    allowedsuits = []
    allowedcolors = []

    alternatehypothesis=""
    even = ['2', '4', '6', '8', '10', 'Q']
    odd = ['A', '3', '5', '7', '9', 'J', 'K']
    if "even" in list:
        allowedvalues = ['2', '4', '6', '8', '10', 'Q']

    if "odd" in list:
        allowedvalues = ['A', '3', '5', '7', '9', 'J', 'K']

    if "Royal" in list:
        allowedsuits = ['A', 'Q', 'J', 'K']

    if 'R' in list:
        allowedcolors =allowedcolors.append('R')
    if 'B' in list:
        allowedcolors =allowedcolors.append('B')

    suitcurrent = extract("Suit", card1)
    valuecurrent = extract("Value", card1)
    colorcurrent = extract("Color", card1)

    suitprevious2 = extract("Suit", card2)
    valueprevious2 = extract("Value", card2)
    colorprevious2 = extract("Color", card2)

    if suitcurrent==suitprevious2:
     if keephypothesis(suitcurrent,"Suit",correct,list)==True:
      alternatehypothesis = alternatehypothesis + "equal(suit(previous2)" + "," + suitcurrent + "))" +"and " +"equal(suit(current)" + "," + suitcurrent + "))"

    if valuecurrent in allowedvalues and valueprevious2 in allowedvalues:
     if valuecurrent in even and valueprevious2 in even:
      if keephypothesis("odd", "Value",correct)==True:
        alternatehypothesis = alternatehypothesis+ "equal(value(previous2)" + "," + "even" + "))" + "and " + "equal(value(current)" + "," + "even" + "))"

     if valuecurrent in odd and valueprevious2 in odd:
      if keephypothesis("even", "Value",correct)==True:
        alternatehypothesis = alternatehypothesis + "equal(value(previous2)" + "," + "odd" + "))" + "and " + "equal(value(current)" + "," + "odd" + "))"

    if valueprevious2 in even and valuecurrent in even:
     if keephypothesis("even", "Value",correct)==True:
      alternatehypothesis =alternatehypothesis + "equal(value(previous2)" + "," + "even" + "))" + "and " + "equal(value(current)" + "," + "even" + "))"

    if valueprevious2 in odd and valuecurrent in odd:
     if keephypothesis("odd", "Value",correct)==True:
      alternatehypothesis = alternatehypothesis +"equal(value(previous2)" + "," + "odd" + "))" + "and " + "equal(value(current)" + "," + "odd" + "))"

    if colorcurrent==colorprevious2:
     if keephypothesis(colorcurrent, "Color",correct)==True:
      print "imhere"
      alternatehypothesis =alternatehypothesis + "equal(color(previous2)" + "," + colorcurrent + "))" + "and " + "equal(color(current)" + "," + colorcurrent + "))"

    if colorcurrent in allowedcolors and  colorprevious2 in allowedcolors:
     if colorcurrent==colorprevious2:
      if keephypothesis(colorcurrent, "Color",correct)==True:
       alternatehypothesis = alternatehypothesis +"equal(color(previous2)" + "," + colorcurrent + "))" + "and " + "equal(value(current)" + "," + colorcurrent + "))"

    if suitcurrent in allowedsuits and suitprevious2 in allowedsuits:
     if keephypothesis(suitcurrent, "Suit",correct)==True:
      alternatehypothesis = alternatehypothesis +"equal(suit(previous2)" + "," + suitcurrent + "))" + "and " + "equal(suit(current)" + "," + suitcurrent + "))"
    hypothesis=hypothesis+ "alternate " + alternatehypothesis
    return alternatehypothesis


def keephypothesis(x,attribute,correct):

 return True
 """even = ['2', '4', '6', '8', '10', 'Q']
 odd = ['A', '3', '5', '7', '9', 'J', 'K']

 if attribute=="Suit":
  for card in correct:
   s=extract(attribute, card)
   if x!=s:
    return False
 if attribute=="Color":
  for card in correct:
    s = extract(attribute,card)
    if x != s:
     return False

 if attribute=="Value":
  s = extract(attribute, card)
  for card in correct:
   if x=="even":
    if s not in even:
     return False
    if x=="odd":
     if x == "even":
      if s not in odd:
        return False

  return"""












def CheckAlternate(wrong,hypothesis,correct,state):

 list=parseRule(hypothesis)


 allcards = state
 #print allcards


 """if len(x)!=0
 for x in wrong:
  hypothesis=checkCard(x,list,hypothesis)"""



 for i  in range(len(state)):
  if allcards[i] in  correct and allcards[i+2] in correct:
    hypothesis=findSimilarity(allcards[i],allcards[i+2],list,hypothesis,correct)

  return hypothesis

wrong=[]
correct=['4S','10H','2S','9H']
state=['4S','10H','2S','9H']

print CheckAlternate(wrong,"(orf(greater(prev,current)))",correct,state)

#print evaluate(CheckAlternate(wrong,"(orf(greater(prev,current),notf(is_royal(current))))",correct,state))















































