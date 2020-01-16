logged_in = True

username = "Atanu"

# These are conditional statements. We'll cover these later, but
# you might be able to make out how they're working here.
if logged_in == True:
    print("Welcome " + username + ", loading launch codes.")
elif logged_in == False:
    print("Sorry, I can't load the launch codes unless you log in.")
else:
    print("Hey pal, no trying to hack the mainframe login.")
