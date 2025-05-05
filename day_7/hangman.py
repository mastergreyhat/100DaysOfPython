import random

words = ["lion", "tiger", "camel"]
chosen_word = random.choice(words)
print(chosen_word)

placeholder = "_" * len(chosen_word)
print(placeholder)

correct_letters = []
display = placeholder

while  display != chosen_word:
    guess = input("\nGuess a letter: ").lower()
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

print("\nCongrats you won the game")


