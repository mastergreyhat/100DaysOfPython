import random
from hangman_resources import words, logo, stages, lives

stages.reverse()
print(logo)

chosen_word = random.choice(words)

placeholder = "_" * len(chosen_word)
print(f"Word to guess: {placeholder}")

correct_letters = []
display = placeholder

while  display != chosen_word and lives != 0:
    print(f"\n***************** {lives}/6 LIVES LEFT *****************")
    guess = input("\nGuess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed the letter '{guess}'")

    if guess not in chosen_word:
        lives -= 1
        print(f"Guessed letter '{guess}' not in the word. You lose a life.")
        print(stages[lives])
    else:
        print(stages[lives])

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
    print(f"\nThe correct word was '{chosen_word}' \nGAME OVER")
    
else:
    print("\nCongrats you won the game!")
