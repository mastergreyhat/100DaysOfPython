import random
from art import logo

def choose_difficulty():
    """Prompts the user to choose a difficulty and returns the number of lives."""
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == "easy":
        return 10
    elif choice == "hard":
        return 5
    else:
        print("Invalid Choice")
        exit()

def play_game(answer, lives):
    """Runs the guessing logic of the game."""
    guess = None
    while guess != answer and lives != 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        # guess = int(input("Make a guess: "))
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            lives -= 1
            continue
        if guess > answer:
            print("Too High.")
            lives -= 1
        elif guess < answer:
            print("Too Low.")
            lives -= 1
        else:
            print(f"You got it! The answer was {answer}")
            exit()
    if lives == 0 and guess != answer:
        print(f"You've run out of guesses. The answer was {answer}.")

print(logo)
answer = random.randint(1, 100)
lives = choose_difficulty()
play_game(answer, lives)