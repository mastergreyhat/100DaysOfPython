import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

all_choices = [rock, paper, scissors]

# player_choice = input("Choose Rock, Paper or Scissor: ").lower()
player_choice = input("What do you choose? Rock, Paper or Scissors: ")

if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
    if player_choice == "rock":
        print(rock)
    elif player_choice == "paper":
        print(paper)
    elif player_choice == "scissors":
        print(scissors)
    
    print("Computer chose: ")
    computer_choice = random.choice(all_choices)
    print(computer_choice)


    if player_choice == "rock" and computer_choice == scissors:
        print("You Win")
    elif player_choice == "rock" and computer_choice == rock:
        print("It's a draw")
    elif player_choice == "rock" and computer_choice == paper:
        print("You lose")
    
    elif player_choice == "paper" and computer_choice == rock:
        print("You Win")
    elif player_choice == "paper" and computer_choice == paper:
        print("It's a draw")
    elif player_choice == "paper" and computer_choice == scissors:
        print("You lose")
    
    elif player_choice == "scissors" and computer_choice == paper:
        print("You Win")
    elif player_choice == "scissors" and computer_choice == scissors:
        print("It's a draw")
    elif player_choice == "scissors" and computer_choice == rock:
        print("You lose")
else:
    print("Invalid Choice")



#efficient way shared by chatgpt using modulus operator:
'''
if (player_choice - computer_choice) % 3 == 1:
    print("You win!")
elif (player_choice - computer_choice) % 3 == 2:
    print("You lose!")
else:
    print("It's a draw!")
'''
