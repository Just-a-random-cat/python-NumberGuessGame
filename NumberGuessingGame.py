import random

def instruction():
    print("----------Python Number Guessing Game----------")
    instructions = ["Guess a number from 1 to 100!",  
                    "Game will continue on running until you win.",      
                    "To win you need to guess the correct number.",
                    "Good luck!"]
    for i in instructions:
        print(f"{i:^47}")       # To center the instructions
    print("-----------------------------------------------")
    print("Difficulty levels:")
    print("1. Easy  (10 Chances)")
    print("2. Medium (5 Chances)")
    print("3. Hard   (3 Chances)")

def amountOfChances():
    levelNumber = input("Select a difficulty level (1-3): ")
    if levelNumber == "1":
        return 10
    elif levelNumber == "2":
        return 5
    elif levelNumber == "3":
        return 3
    
def mainGame(correctNumber, chances):
    originalChances = chances
    guessedNumbers = set()              # For storing numbers that have already been guessed

    while chances > 0:
        try:
            print("-----------------------------------------------")
            guessNumber = int(input("Guess the number: "))
        except ValueError: 
            print("Enter only numbers please")
            continue

        if guessNumber in guessedNumbers:
            print(f"You have already guessed {guessNumber}")
        elif guessNumber == correctNumber:
            print("You guessed correctly!")
            print(f"The number was {correctNumber}")
            print(f"It took you {originalChances - chances} chances to guess")
            break
        else:
            guessedNumbers.add(guessNumber)
            chances -= 1
            print("That is not the correct number.")
            print("The correct number is higher" if correctNumber > guessNumber else "The correct number is lower.")
            print(f"You have {chances} chances left.")

        if chances == 0:
            print(f"You couldn't guess the number within {originalChances} chances")
            print(f"The correct number was {correctNumber}.")
            print("-----------------------------------------------")


while True:
    instruction()

    chances = amountOfChances()
    correctNumber = random.randint(1, 100)

    mainGame(correctNumber, chances)
    decision = input("Would you like to continue playing? (Y/N): ").capitalize()

    if decision == "N":
        break