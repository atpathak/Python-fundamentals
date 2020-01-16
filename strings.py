food = "ham"

type_of_food = type(food)
print(type_of_food)

first_letter = food[0]
second_letter = food[1]
print("The first letter is " + first_letter)
print("The second letter is " + second_letter)

print(len(food))

superfood = food + " and eggs"
print("I like " + superfood)

name = "Guido"
cost = 3
demand = "Bring me {} shrubberies, {}!"
print(demand.format(cost, name))
