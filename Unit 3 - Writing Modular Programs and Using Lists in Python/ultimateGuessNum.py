import random

# Global Variables
lowerBound = 0
upperBound = 0
n = 0
secret_number = 0

# Initialize the Game
def initialGame():
    global lowerBound, upperBound, n, secret_number
    lowerBound = 1
    upperBound = 100
    n = 10
    secret_number = random.randint(lowerBound, upperBound)

# Show Game Information
def showGameInfo(n, lowerBound=1, upperBound=100):
    print("This game is Developed during the ICS3U class")
    print("#"*50)
    print()

    print('We are playing a Guessing Number Game.')
    print('The Number is from', lowerBound, ' to ', upperBound)
    print('You have a total of', n, "chances.")

# Check The number
# Parameter: guess - the current guess
# - Return a postive Value if the guess is Larger
# - Return a negative Value if the guess is Smaller
# - Return 0 if the Guess is Correct
def checkNumber(guess):
    return guess - secret_number

# Print Loss, if the remaining chances is 0 and the Guess is not Correct.
# Parameter: guess - the current guess
def checkLoss(n, guess):
    if n == 0 and guess != secret_number:
        print("You Lose!")
        print("The number is ", secret_number)

# The Game function.
# Parameter: attemps - number of chances
def Game(attemps):
    n = attemps
    while n != 0:
        guess = int(input("Your Guess: "))
        check = checkNumber(guess)
        if check < 0:
            print("Your number is smaller!")
        elif check > 0:
            print("Your number is bigger!")
        else:
            print("Your Number is Correct. You Win!")
            break
        n = n - 1
        print("Your remaining chances: ", n)
        print() #chance line for nice formate
    checkLoss(n, guess)

def main():

    initialGame()

    showGameInfo(n, lowerBound, upperBound)

    Game(n)

main()