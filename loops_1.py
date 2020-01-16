for character in "Howdy":
    print(character)
    
# Ranges.
for n in range(10):
    print("n is: {}".format(n))
    
# Dictionaries (more on these later).
user = {
    "name": "Grae",
    "role": "admin",
    "age": 35
}

for property in user:
    print(property)
    
# We can also do more than just print things.
even_numbers = []
odd_squares = []

for n in range(10):
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_squares.append(n ** 2)

print(even_numbers)
print(odd_squares)
