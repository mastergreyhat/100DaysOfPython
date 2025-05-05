import random

hangman = [r"""
  +---+
  |   |
      |
      |
      |
      |
=========""", r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""", r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

hangman.reverse()

words = ["lion", "tiger", "camel"]
lives = 6
chosen_word = random.choice(words)
print(chosen_word)

placeholder = "_" * len(chosen_word)
print(placeholder)

correct_letters = []
display = placeholder

while  display != chosen_word and lives != 0:
    guess = input("\nGuess a letter: ").lower()

    if guess not in chosen_word:
        lives -= 1
        print(hangman[lives])
        print(f"{lives} lives remaining")
    else:
        print(hangman[lives])

    display = ""
    for ch in chosen_word:
        if ch == guess:
            display += guess
            correct_letters.append(guess)
        elif ch in correct_letters:
            display += ch
        else:
            display += "_"
    print(display)

if lives == 0:
    print(f"The correct word was {chosen_word}")
    print("You Lose... Game Over")
    
else:
    print("\nCongrats you won the game")


