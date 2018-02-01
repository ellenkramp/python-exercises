tally = 0
coins = raw_input("Do you want a coin? y/n ")
while coins == 'y':
    tally +=1
    print "You have %d coins! " % tally
    coins = raw_input("Do you want another? y/n ")
else:
    print "Bye!"


    
