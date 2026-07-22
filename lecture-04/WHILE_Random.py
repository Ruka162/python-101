import random
print("Random numbers between 1 and 100:")
mynumber = random.randint(1, 100)
ntries = 1
yourguess = -1
while ntries < 7 and yourguess != mynumber:
    msg = str(ntries) + ">>"
    if (ntries == 6):
        msg = "Last chance>>"
    yourguess = int(input(msg))
    if yourguess > mynumber:
        print("Too high")
    elif yourguess < mynumber:
        print("Too low")
        ntries += 1
if yourguess == mynumber:
    print("You got it!")
else:
    print("Sorry, the number was " + str(mynumber))