raw_input("Press <ENTER> To Begin")
    print "You have $",money,"in your bank."
    bet = raw_input("How much would you like to bet?")

    b = int(bet)

    cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
	# At a time two cards are drawn
    c1 = choice(cards)
    cards.remove(c1) 

    c2 = choice(cards)
    cards.remove(c2)

    psum = c1 + c2 # Player's sum of the cards

    print "You were dealt a",c1,"and a",c2,"for a sum of",psum,
    print "\n"
    hs = " " # Hit / Stand

    while psum < 21 and "s" not in hs:
        hs = raw_input("Hit or Stand (h or s): ").lower()
        if "h" in hs:
            c3 = choice(cards)
            cards.remove(c3)
            psum = psum + c3 # another card dealt
            print "You were dealt a",c3,"for a sum of",psum,
            print "\n"
        elif "s" in hs: # Standing
            print "Your final sum is",psum,

    print "\n"

    if psum > 21:
        print "Bust!" "\n" "You lose." "\n"
        money = money - b
        print "You now have $",money,"in your bank."
    elif psum == 21:
        print "You got a BlackJack!" "\n" "You win!" "\n"
        money = money + b
        print "You now have $",money,"in your bank."   
    else:
        print "Dealer's turn"

    if psum < 21:    # If psum<21 so dealer can play
        c4 = choice(cards)
        cards.remove(c4) 

        c5 = choice(cards)
        cards.remove(c5)

        dsum = c4 + c5 # Dealer's sum of cards

        while dsum < 17: # If dsum <17 then dealer dealt with another card
            c6 = choice(cards)
            cards.remove(c6)
            dsum = dsum + c6

        if dsum > 21:
            print "Dealer's final sum is",dsum,"\n"
            print "Dealer bust! You win!" "\n"
            money = money + b
            print "You now have $",money,"in your bank."
        elif dsum < psum:
            print "Dealer's final sum is",dsum,"\n"
            print "You win!" "\n"
            money = money + b
            print "You now have $",money,"in your bank."
        elif dsum == psum:
            print "Dealer's final sum is",dsum,"\n" 
            print "Draw." "\n"
            print "You have $",money,"in your bank."
        else:
            print "Dealer's sum is",dsum,"\n"
            print "You lose." "\n"
            money = money - b
            print "You now have $",money,"in your bank."


    yn = raw_input("Would you like to play again? (y or n): ")

    if "y" in yn:
        print "\n" * 5
        run()
    else:
        print "\n" "Your total winnings is $",money,
        sys.exit()   