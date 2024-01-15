print("Welcome to My Computer Quiz!")
playing = input("Do you want to play?")
if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0
answer = input("What does A stands for? ")
if answer[0].lower() == "a":
    print("Correct, you got 5 points")
    score += 5
else:
    print("Incorrect")


answer = input("What does B stands for? ")
if answer[0].lower() == "b":
    print("Correct, you got 5 points")
    score += 5
else:
    print("Incorrect")


answer = input("What does C stands for? ")
if answer[0].lower() == "c":
    print("Correct, you got 5 points")
    score += 5
else:
    print("Incorrect")


answer = input("What does D stands for? ")
if answer[0].lower() == "d":
    print("Correct, you got 5 points")
    score += 5
else:
    print("Incorrect")


answer = input("What does E stands for? ")
if answer[0].lower() == "e":
    print("Correct, you got 5 points")
    score += 5
else:
    print("Incorrect")


print("your score is " + str(score))
print("you got ", (score/25)*100, " %")
