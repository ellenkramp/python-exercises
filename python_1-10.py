
#ten = range(1,11)

#start = int(raw_input("What number should we start with? "))
#end = int(raw_input("What number should we end with?" ))
#for x in ten:
#  if start<=x<=end:
#    print x

#for x in range(1,10):
 #   if x%2>0:
  #      print x

tally = 0
coin = raw_input("Do you want a coin? y/n ")
if coin == 'y':
    tally += 1
    print "You have %d coins." % tally
    another = raw_input("Do you want another? y/n ")
    while another == 'y':
        tally += 1
        print "You have %d coins." % tally
        another = raw_input("Do you want another? y/n ")
        if another == 'n':
            print "Bye"
elif coin == 'n':
    print "Bye"
else:
    print "Not valid. Goodbye"
