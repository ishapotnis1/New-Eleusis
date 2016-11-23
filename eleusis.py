#taking cards from the user
def enter_card():
    cards=[]
    print "Enter the cards as '3H' where 3 is a card of hearts"
    for i in range(0,3):
        cards.append(raw_input("Enter the card"))
    print cards
enter_card()
