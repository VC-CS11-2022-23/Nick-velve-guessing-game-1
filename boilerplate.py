TRIES = 0
import random
#This imports a random number between 1 and 10
number = random.randint(1,10)
while TRIES < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    #This is meant to count the number of tries so when it reaches the limit of 3 it will stop
    TRIES = TRIES + 1
    if guess == number:
        print("correct")
     #This portion will break the loop to show that the game has ended. The print stuff is there to show if you got it right or not.
        break
    if guess > number:
        print("too high")
    else:
        print("too low")
    #This is to show that the game will end after 3 tries 
if TRIES == 3:
    print("That was your last try! ")