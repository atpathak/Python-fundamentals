# Here's a super simple dictionary:
person = {"name": "grae", "profession": "magician"}

# Dictionaries are great for grouping related data together.
# Let's make a dictionary with more data.

# Note how we split each key-value pair onto a new line. This
# can make dictionaries much easier to read.
hero = {
    "name": None,
    "species": "Human",
    "strength": 4,
    "magic": 5,
    "profession": "Student",
}

# Let's check the hero's name again. Just like lists, we use
# bracket notation.
if hero["name"] is None:
    # We modify dictionary values just like we access them.
    hero["name"] = input("What is your name?")
    print("Fantastic, thanks {}".format(hero["name"]))

# You can also add a new key-value pairs using the same bracket
# notation syntax.
hero["favorite_color"] = "Octarine"
print(hero["favorite_color"])

# Try inserting a line of code below this comment that changes
# the hero's `profession` from `None` to another value so the next
# print statement works well.

print("Ok {}, you are a {} {}.".format(hero["name"], hero["species"], hero["profession"]))

