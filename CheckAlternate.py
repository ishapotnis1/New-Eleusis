#  (is_royal(current), False)
import re
correct=[]
wrong=["4H","5S"]
prev="5H"
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
    print rule


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



def findRule(hypothesis):
 list=hypothesis.split("),")
 return list




def checkCard(card,list,hypothesis,prev,current):


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

  if "prev" in list:
   suitprev = extract("Suit", prev)
   valueprev = extract("Value", prev)
   colorprev = extract("Color", prev)

  if suitcurrent in allowedsuits:
   hypothesis=hypothesis+ "AND "+"equal(suit(current),"+ ","+suitcurrent+"))"

  if valuecurrent in allowedvalues:
   x=""
   if valuecurrent in even:
    x="even"
   if valuecurrent in odd:
    x="odd"
   hypothesis = hypothesis + "AND "+x

  if colorcurrent in list:
   hypothesis = hypothesis +"and "+ "equal(color(current),"+ ","+colorcurrent+"))"

  return hypothesis



def CheckAlternate(wrong,hypothesis):

 list=parseRule(hypothesis)
 for x in wrong:
  hypothesis=checkCard(x,list,hypothesis,"2H","3H")

 return hypothesis

#print  CheckAlternate(wrong,"( orf(equal(color(current),B),greater(prev,current)) ,True)")



















































