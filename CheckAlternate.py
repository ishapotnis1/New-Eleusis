#  (is_royal(current), False)
import re


import pyparsing # make sure you have this installed

map={}

threshold={}
threshold['Suit']=0
threshold['Color']=0
threshold['Value.odd']=0
threshold['Value.even']=0
threshold['Royal']=0


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
  Value=card[0]

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


def findSimilarity(cards,card1,card2,list,hypothesis,correct,threshold):
    allowedvalues = []
    allowedsuits = []
    allowedcolors = []

    alternatehypothesis={}
    alternatehypothesis['Suit']=""
    alternatehypothesis['Value.even']=""
    alternatehypothesis['Value.odd']=""
    alternatehypothesis['Color']=""
    alternatehypothesis['Royal'] = ""

    Royal=['J','K','Q','A']
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
    print  valuecurrent


    suitprevious2 = extract("Suit", card2)
    valueprevious2 = extract("Value", card2)
    colorprevious2 = extract("Color", card2)

    if suitcurrent==suitprevious2:
     threshold['Suit']=threshold['Suit']+1
     alternatehypothesis['Suit'] = alternatehypothesis['Suit'] + "(equal(suit(previous2)" + "," + suitcurrent + "))" +"," +"equal(suit(current)" + "," + suitcurrent + ")))"

    if valuecurrent in allowedvalues and valueprevious2 in allowedvalues:
     if valuecurrent in even and valueprevious2 in even:

      threshold['Value'] =   threshold['Value']+1
      alternatehypothesis['Value.even'] = alternatehypothesis['Value.even']+ "(equal((even(previous2)" +  ',' + "equal(even(current)))"

     if valuecurrent in odd and valueprevious2 in odd:
      threshold['Value.odd'] = threshold['Value.odd'] + 1
      alternatehypothesis['Value.odd'] = alternatehypothesis['Value.odd']+ "(equal((odd(previous2)" +  ',' + "equal(odd(current)))"

    if valueprevious2 in even and valuecurrent in even:
     threshold['Value.even'] = threshold['Value.even'] + 1
     alternatehypothesis['Value.even'] = alternatehypothesis['Value.even'] +"(equal((even(previous2)" +  ',' + "equal(even(current)))"
    if valueprevious2 in odd and valuecurrent in odd:
     threshold['Value.odd'] = threshold['Value.odd'] + 1
     alternatehypothesis['Value.odd'] = alternatehypothesis['Value.odd']+"(equal((odd(previous2)" +  ',' + "equal(odd(current)))"

    if colorcurrent==colorprevious2:
     threshold['Color'] = threshold['Color'] + 1
     alternatehypothesis['Color'] = alternatehypothesis['Color']+ "(equal(color(previous2)" + "," + colorcurrent + "))" + "," + "equal(color(current)" + "," + colorcurrent + ")))"

    if colorcurrent in allowedcolors and  colorprevious2 in allowedcolors:
     if colorcurrent==colorprevious2:
      threshold['Color'] = threshold['Color'] + 1
      alternatehypothesis['Color'] = alternatehypothesis['Color'] +"(equal(color(previous2)" + "," + colorcurrent + "))" + ", " + "equal(value(current)" + "," + colorcurrent + ")))"

    if suitcurrent in allowedsuits and suitprevious2 in allowedsuits:
     threshold['Suit'] = threshold['Suit'] + 1
     alternatehypothesis['Suit'] = alternatehypothesis['Suit'] +"(equal(suit(previous2)" + "," + suitcurrent + "))" + "," + "equal(suit(current)" + "," + suitcurrent + ")))"

    if valuecurrent in Royal and valueprevious2 in Royal:
     threshold['Royal'] = threshold['Royal'] + 1
     alternatehypothesis['Royal'] = alternatehypothesis['Royal'] +"(is_Royal(suit(previous2)" + "," + "Royal" + "))" + "," + "equal(is_Royal(current)" + "," + "Royal" + ")))"


    alter=""

    if len(cards)>6:
     if threshold['Suit']>=2:
      alter=alter+","+alternatehypothesis['Suit']
     if threshold['Color'] >= 2:
      alter = alter +","+ alternatehypothesis['Color']
     if threshold['Value.odd']>=2:
      alter = alter +","+  alternatehypothesis['Value.odd']
     if threshold['Value.even'] >= 2:
      alter = alter  +","+  alternatehypothesis['Value.even']
     if  threshold['Royal'] >= 2:
      alter = alter +","+ alternatehypothesis['Royal']

    else:
     alter=alternatehypothesis['Suit'] +","+ alternatehypothesis['Color'] +","+  alternatehypothesis['Value.odd'] +","+ alternatehypothesis['Value.even'] +","+ alternatehypothesis['Royal']

    alter="andf"+'('+alter+')'
    print threshold



    return alter




def CheckAlternate(wrong,hypothesis,correct,state):

 list=parseRule(hypothesis)


 allcards = state
 #print allcards


 """if len(x)!=0
 for x in wrong:
  hypothesis=checkCard(x,list,hypothesis)"""



 for i  in range(0,len(state)):
  if i+2<len(state):
   if allcards[i] in  correct and allcards[i+2] in correct:
    hypothesis=findSimilarity(state,allcards[i],allcards[i+2],list,hypothesis,correct,threshold)



 return hypothesis

wrong=[]
correct=['JD','JS','KS','KS','QS','JD','9D']
state=['JS','10D','JD','9D','KS','10D','QS','9D','JD']

print CheckAlternate(wrong,"(orf(greater(prev,current)))",correct,state)

#print evaluate(CheckAlternate(wrong,"(orf(greater(prev,current),notf(is_royal(current))))",correct,state))















































