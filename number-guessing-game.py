
import random
import math

print("Welcome to the number guessing game. Lets play!")

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
randomNumber = random.randint(lower,upper)

chances = int(math.log2(upper-lower+1)) + 1
guess_counter = 0
chances_count= chances

print(f"You will have {chances} chances to guess")

while guess_counter < chances:
    print("--------------------------------")
    print(f"Chances left: {chances_count}")
    chances_count -=1
    guess_counter +=1
    guess = int(input("Enter your guessing number: "))

    if guess == randomNumber:
        print(f"***The number is {randomNumber} and you found it right !! in {guess_counter} attempts!***")
        break
    elif guess_counter >= chances and guess != randomNumber:
        print(f"Oops, the number is {randomNumber}, better luck next time!")
    elif guess < randomNumber:
        print("Try Again! You guessed too small")
    elif guess > randomNumber:
        print("Try Again! You guessed too high")



