import random
from data import logo, vs, data

game_over = False
score = 0

random_A = random.choice(data)
random_B = random.choice([item for item in data if item != random_A])

while game_over == False:
    print(logo)
    print(f"Compare A: {random_A['name']}, a {random_A['description']}, from {random_A['country']}.")
    print(vs)
    print(f"Compare B: {random_B['name']}, a {random_B['description']}, from {random_B['country']}.")
    pick = input("Who has more followers? Type 'A' or 'B': ")
    
    if (pick == 'A' and random_A['follower_count'] > random_B['follower_count']) or (pick == 'B' and random_B['follower_count'] > random_A['follower_count']):
        score += 1
        print(f"You're right! Current score: {score}")
        random_A = random_B
        random_B = random.choice([item for item in data if item != random_A])
    else:
        print(f"Sorry that's the wrong answer. Final score: {score}")
        game_over = True
