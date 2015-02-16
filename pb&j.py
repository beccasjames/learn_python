#First goal is below: create a program that can tell you whether or not you can make a pb&j

slices_bread = 2
sandwiches_pb = 1
sandwiches_jelly = 1

if slices_bread >= 2 and sandwiches_pb >= 1 and sandwiches_jelly >= 1:
    print "You can make a sandwich!"
else:
    print "You need to go shopping."
        
#Second goal is below: create a program that can tell you how many sandwiches you can make

slices_bread = 4
sandwiches_pb = 2
sandwiches_jelly = 2

if slices_bread >= 2 and sandwiches_pb >= 1 and sandwiches_jelly >= 1:
    total = slices_bread / 2
    if sandwiches_pb <= total:
        total = sandwiches_pb
    if sandwiches_jelly <= total:
        total = sandwiches_jelly
    print "You can make {0} sandwiches!".format(total)
else:
    print "No peanut butter and jelly sandwiches for you!"
    
# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread

slices_bread = 5
sandwiches_pb = 3
sandwiches_jelly = 2

if slices_bread >= 2 and sandwiches_pb >= 1 and sandwiches_jelly >= 1:
    total = slices_bread / 2
    if sandwiches_pb < total:
        total = sandwiches_pb
    if sandwiches_jelly < total:
        total = sandwiches_jelly
    print "I can make {0} sandwiches!".format(total)
    if slices_bread % 2 == 1:
        print "You can make an open-faced sandwich, too."
else:
    print "No peanut butter and jelly sandwiches for you!"
    
# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

slices_bread = 0
sandwiches_pb = 1
sandwiches_jelly = 2

if slices_bread >= 2 and sandwiches_pb >= 1 and sandwiches_jelly >= 1:
    total = slices_bread / 2
    if sandwiches_pb < total:
        total = sandwiches_pb
    if sandwiches_jelly < total:
        total = sandwiches_jelly
    print "I can make {0} sandwiches!".format(total)
    if slices_bread % 2 == 1:
        print "You can make an open-faced sandwich."
else:
    print "No peanut butter and jelly sandwiches for you!"
    if slices_bread < 2:
        print "You don't have enough bread!"
    if sandwiches_pb < 1:
        print "You don't have enough peanut butter!"
    if sandwiches_jelly < 1:
        print "You don't have enough jelly!"
        
# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.

slices_bread = 2
sandwiches_pb = 1
sandwiches_jelly = 1

if slices_bread >= 2 and sandwiches_pb >= 1 and sandwiches_jelly >= 1:
    total = slices_bread / 2
    if sandwiches_pb < total:
        total = sandwiches_pb
    if sandwiches_jelly < total:
        total = sandwiches_jelly
    print "I can make {0} sandwiches!".format(total)
    if slices_bread % 2 == 1:
        print "You can make an open-faced sandwich."
    if slices_bread / 2 > sandwiches_jelly and sandwiches_pb > sandwiches_jelly:
        if slices_bread / 2 > sandwiches_pb:
            print "You can make {0} peanut butter sandwiches.".format(sandwiches_pb - sandwiches_jelly)
        else:
            print "You can make {0} peanut butter sandwiches, but please don't because you're allergic.".format(slices_bread / 2 - sandwiches_jelly)