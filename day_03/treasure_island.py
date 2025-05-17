print('''
 _                                         _     _                 _ 
| |                                       (_)   | |               | | 
| |_ _ __ ___  __ _ ___ _   _ _ __ ___     _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \   | / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/   | \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|   |_|___/_|\__,_|_| |_|\__,_|
      
''')

print("Welcome to Treasure Island !")
choice_1 = input("You're at a cross road. Where do you want to go!\n  Type \"left\" or \"right\": ").lower()       #lower() converts the input to lowercase

if choice_1 == "left":
    choice_2 = input("You've come to a lake. There is an island in the middle of the lake.\n  Type \"wait\" to wait for a boat. Type \"swim\" to swim across: ").lower()
    if choice_2 == "wait":
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors.\n  Which door would you choose \"red\", \"yellow\" or \"green\": ").lower()
        if choice_3 == "yellow":
            print("Congrats... you have found the Treasure and won the game!")
        elif choice_3 == "red":
            print("You entered room filled with fire...\nGAME OVER")
        elif choice_3 == "green":
            print("You entered a room full of beasts...\nGAME OVER")
        else:
            print("You chose a door which doesn't exist...\nGAME OVER")
    elif choice_2 == "swim":
        print("You were devoured by crocodiles...\nGAME OVER")
    else:
        print("Invalid choice...\nGAME OVER")
elif choice_1 == "right":
    print("You fell into a pit...\nGAME OVER")
else:
    print("Invalid choice...\nGAME OVER")