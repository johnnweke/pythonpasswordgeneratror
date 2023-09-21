#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Letters
password_letter =""
for char in range(1, nr_letters + 1):
  random_char = random.choice(letters)
  password_letter += random_char
# print(password_letter)
  
# Numbers
password_number = ""

for number in range(1, nr_numbers + 1):
  random_number = random.choice(numbers)
  password_number += random_number
  

#Symbols
password_symbol = ""
for symbol in range (1, nr_symbols + 1):
  random_symbol = random.choice(symbols)
  password_symbol += random_symbol

#Total

joined_password = password_letter + password_number + password_symbol
print(f"Easy password is {joined_password}")

  
  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Use the number given to you by the user as a random range

password_list = []
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
  
# Numbers
for number in range(1, nr_numbers + 1):
   password_list.append(random.choice(numbers))
  
#Symbols

for symbol in range (1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

# Shuffle the Password
random.shuffle(password_list)
# print(password_list)

#join the password back together
hard_password = ""
for char in password_list:
  hard_password += char

print(f"Hard password is {hard_password}")
  

