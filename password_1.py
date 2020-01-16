password = ""
failed_attempts = 0
while password != "hunter2":
    password = input("what is the password?")
    if password == "hunter2":
        print("Correct!")
    else:
        print("I'm sorry, that's not correct.")
        failed_attempts += 1
        print("Wrong guesses: {}".format(failed_attempts))

