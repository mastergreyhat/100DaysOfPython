import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*']

print("Welcome to PyPassword Generator!\n")
letter_num = int(input("How many letters would you like in your password: "))
number_num = int(input("How many numbers would you like: "))
symbol_num = int(input("How many symbols would you like: "))

password_list = []

for letter in range(letter_num):
    password_list += random.choice(letters)
for number in range(number_num):
    password_list += random.choice(numbers)
for symbol in range(symbol_num):
    password_list += random.choice(symbols)

random.shuffle(password_list)

final_password = ""

for char in password_list:
    final_password += char

print(f"\nYour final password is: {final_password}")



#Solution using random sample, shuffle and join
'''
random_letters = random.sample(letters, letter_num)
random_numbers = random.sample(numbers, number_num)
random_symbols = random.sample(symbols, symbol_num)

password_list = random_letters + random_numbers + random_symbols
random.shuffle(password_list)
final_password = ''.join(password_list)
print(final_password)
'''