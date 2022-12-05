TRIES = 0
import random
number = random.randint(1,10)
while TRIES < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    TRIES = TRIES + 1
    if guess == number:
        print("correct")
        break
    if guess > number:
        print("too high")
    else:
        print("too low")
if TRIES == 3:
    print("That was your last try! ")