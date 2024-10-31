import random

name = input("What is your name?: ")
print(f"Good luck!, {name}")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the characters")
guesses = ''
turns = 12


while turns > 0:
    failed = 0 
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else: 
            print("_",end=" ")
            failed +=1
    print()
    if failed == 0:
        print("You Win!")
        print(f"The word is: {word}")   
        break

    print()
    guess = input("Enter a character: ")
    guesses += guess

    if guess not in word:
        turns -=1
        print("Wrong")
        print(f"You have {turns} more turns")
    
        if turns == 0:
            print("You Lose!")

