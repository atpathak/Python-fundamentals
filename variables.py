# Ask the user for input and store the result in a variable.
bottle_count = int(input("How many bottles of beer are on the wall?"))

print("There are {} bottles of beer on the wall.".format(bottle_count))

if input("Would you like to take any down?") == "yes":
    removed_bottles = int(input("Ok, how many?"))
    bottle_count = bottle_count - removed_bottles
    print("There are now {} bottles on the wall".format(bottle_count))
else:
    print("Ok, there are still {} bottles on the wall.".format(bottle_count))

