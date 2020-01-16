name = None
species = "Human"
strength = 4
magic = 5
favorite_color = "Octarine"
profession = None

# Hm, maybe we haven't assigned a name yet...
if name is None:
    name = input("What is your name?")
    print("Fantastic, thanks {}".format(name))

# Every adventurer needs a profession.
if profession is None:
    print("{}, you are a {} who needs a profession".format(name, species))
    print("Your strength is {} and magic is {},".format(strength, magic))
    print("and your favorite color is {}".format(favorite_color))
    profession = input("What profession would you like?")

print("Welcome, {}. You are a {} {}.".format(name, species, profession))

