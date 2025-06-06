import random
from art import logo
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    # 11 for ace and three 10s for King, Queen and Jack
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a Draw"
    elif user_score == 0:
        return "You won with a Blackjack"
    elif computer_score == 0:
        return "You lose, Computer won with a Blackjack"
    elif user_score > 21:
        return "You went over and lost"
    elif computer_score > 21:
        return "Computer went over, You win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")
    
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Press 'y' to continue and 'n' to stop: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand was {user_cards}, final score {user_score}")
    print(f"Computer's final hand was {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))
    
while input("Do you want to play a game of blackjack, type 'y' or 'n': ") == 'y':
    clear_screen()
    play_game()
