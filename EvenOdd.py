def modulo_five(num):
    try:
        result = num % 5
        return "{} modulo 5 is {}".format(num, result)
    except TypeError:
        return "{} isn't even a number!".format(num)
    

# Everything works fine when you pass an integer in as expected.
print(modulo_five(42))

# Floats are fine too.
print(modulo_five(3.414))

# Yay, we're properly handling exceptions and using them to
# control which code is executed.
print(modulo_five("Chaos Monkey"))
