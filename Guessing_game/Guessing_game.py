Name = input("Enter your name: ")
print("Hello " + Name + "! Welcome to the guessing game.")
GuessWord = "giraffe"
Guess = ""
GuessCount = 0
GuessLimit = 3
OutOfGuesses = False    
while Guess != GuessWord and not(OutOfGuesses):
    if GuessCount < GuessLimit:
        Guess = input("Enter your guess: ")
        GuessCount += 1
    else:
        OutOfGuesses = True
if OutOfGuesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")