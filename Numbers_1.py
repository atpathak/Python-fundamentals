# Start by assigning some numbers to our variables.
count = 3
pi = 3.14

# Let's see what the built-in `type()`function does.
type_of_count = type(count)
type_of_pi = type(pi)
print(type_of_count)
print(type_of_pi)

# We can do math with numbers. The `%` operator is modulo.
print(count + 2)
print(count * 10 )
print(count / 2)
print(1337 % 2)

# Putting an int and a float together will give you a float.
print(count * pi)

# Be careful with floating point math.
print(.2 + .4)

# Numbers are *not* strings, even if they look similar.
print(10 == "10")


print("Bring me " + str(count) + " shrubberies!")
