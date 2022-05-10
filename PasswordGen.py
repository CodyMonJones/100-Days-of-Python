import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PysWord Generator!")
letter_count = int(input("How many letters would you like in your password?: "))
number_count = int(input("How many numbers would you like in your password?: "))
symbol_count = int(input("How many symbols would you like in your password?: "))

password_list = []
password_string = ""

for letter in range(0, letter_count):
    password_list.append(letters[random.randint(0, len(letters) - 1)])

for number in range(0, number_count):
    password_list.append(numbers[random.randint(0, len(numbers) - 1)])

for symbol in range(0, symbol_count):
    password_list.append(symbols[random.randint(0, len(symbols) - 1)])

random.shuffle(password_list)
print(password_string.join(password_list))    
