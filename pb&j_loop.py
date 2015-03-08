# Difficulty level: Beginner

# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

slices_bread = 8
sandwiches_bread = slices_bread/2
sandwiches_pb = 10
sandwiches_jelly = 4
sandwiches = 0

while slices_bread >= 2 and sandwiches_pb >= 1 and sandwiches_jelly >= 1:
	sandwiches = sandwiches + 1
	print "Making sandwich #{0}".format(sandwiches)
        sandwiches_bread = sandwiches_bread - 1
        sandwiches_pb = sandwiches_pb - 1
        sandwiches_jelly = sandwiches_jelly - 1
        print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more sandwiches, and enough jelly for {2} more sandwiches.".format(sandwiches_bread, sandwiches_pb, sandwiches_jelly)

print "Done making sandwiches. I made {0} sandwiches in total.".format(sandwiches)

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.

slices_bread = 10
sandwiches_bread = slices_bread/2
sandwiches_pb = 2
sandwiches_jelly = 2
sandwiches = 0

while slices_bread >= 2 and sandwiches_pb >= 1 and sandwiches_jelly >= 1:
	sandwiches = sandwiches + 1
	print "Making sandwich #{0}".format(sandwiches)
        sandwiches_bread = sandwiches_bread - 1
        sandwiches_pb = sandwiches_pb - 1
        sandwiches_jelly = sandwiches_jelly - 1
        print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more sandwiches, and enough jelly for {2} more sandwiches.".format(sandwiches_bread, sandwiches_pb, sandwiches_jelly)

print "Done making sandwiches. I made {0} sandwiches in total.".format(sandwiches)

##How do I get this list to add multiple items to it while using if conditionals?

limiting_reagent = []
if sandwiches_bread <= 0:
    limiting_reagent.append("bread")
elif sandwiches_pb <= 0:
    limiting_reagent.append("peanut butter")
elif sandwiches_jelly <= 0:
    limiting_reagent.append("jelly")

if len(limiting_reagent) == 1:
    print "I ran out of {0}.".format(limiting_reagent[0])
elif len(limiting_reagent) == 2:
    print "I ran out of {0} and {1}.".format(limiting_reagent[0], limiting_reagent[1])
elif len(limiting_reagent) == 3:
    print "I ran out of {0}, {1} and {2}.".format(limiting_reagent[0], limiting_reagent[1], limiting_reagent[2])
