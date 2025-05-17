import random

stages = [r"""
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

stages.reverse()

words = ["lion", "tiger", "camel"]
lives = 6
chosen_word = random.choice(words)
print(chosen_word)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("\nGuess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")
    
    if "_" not in display:
        game_over = True
        print("You Win!")

    print(stages[lives])


