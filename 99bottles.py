# Difficulty Level: Beginner

# Can you make Python print out the song for 99 bottles of beer on the wall?

# Using range() and a loop, print out the song.  Your output should look like this:

for bottle in range(99, 0, -1):
    if bottle >= 2:
        print "{0} bottles of beer on the wall, {0} bottles of beer...".format(bottle)
        if bottle-1 >= 2:
            print "If one of those bottles should happen to fall, {0} bottles of beer on the wall.".format(bottle-1)
        elif bottle-1 == 1:
            print "If one of those bottles should happen to fall, {0} bottle of beer on the wall.".format(bottle-1)
    elif bottle == 1:
        print "{0} bottle of beer on the wall, {0} bottle of beer...".format(bottle)
        print "If that bottle should happen to fall, no more bottles of beer on the wall!"

# 99 bottles of beer on the wall, 99 bottles of beer ...
# If one of those bottles should happen to fall, 98 bottles of beer on the wall
# 98 bottles of beer on the wall, 98 bottles of beer ...
# If one of those bottles should happen to fall, 97 bottles of beer on the wall
# ...
