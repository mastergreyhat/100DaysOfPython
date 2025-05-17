import os
from art import logo

print(logo)

proceed = True

bid_book = {}

while proceed:
    name = input("What is your name?: ")          # key
    bid = int(input("What's your bid?: $ "))      # value
    bid_book[name] = bid
    option = input("Do you want to continue? Type 'yes' or 'no': ").lower()
    # Clear command depending on the OS
    os.system('cls' if os.name == 'nt' else 'clear')
    if option == "yes":
        proceed = True
    else:
        proceed = False

highest_bidder = ""
highest_bid = 0

for bidder in bid_book:
    if bid_book[bidder] > highest_bid:
        highest_bid = bid_book[bidder]
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of $ {highest_bid}")