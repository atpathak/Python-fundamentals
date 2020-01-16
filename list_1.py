# Start by assigning some lists to variables.
inventory = ["beans", "coin", "tome"]
tome_dimensions = [8.5, 11, 2]

# Lists in lists...
random_stuff = [True, 3.14, ["pie", "pizza", "automobile"]]
battleship_board = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]

# Just like with strings you can access list elements by index
# with bracket notation. We start counting at zero:
print(inventory[0])
print(random_stuff[2])

# With nested lists you can continue digging down with additional
# indexes:
print(random_stuff[2][0])

# Lists have a particular length.
inventory_size = len(inventory)
print("You have {} items in your inventory".format(inventory_size))

# Lists are easy to modify. We'll cover this in more detail later.
inventory.append("magic sword")
print(inventory)

