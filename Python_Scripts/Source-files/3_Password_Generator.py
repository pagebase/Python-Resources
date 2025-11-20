import random
import pyperclip # This module copy data into your clipboard

upper_letters=[chr(letter) for letter in range(65,91)]
lower_letters=[chr(letter) for letter in range(97, 123)]
numbers=[chr(num) for num in range(48, 58)]
symbols=[chr(sym) for sym in range(33, 48)]
password_list=[]

# Ask user how many upper letters he/she wants
upper_letter_choice=int(input("How many upper case do you want?: ").strip())
lower_letter_choice=int(input("How many lower case do you want?: ").strip())
numbers_choice=int(input("How many numbers do you want?: ").strip())
symbol_choice=int(input("How many symbols do you want?: ").strip())

# Add upper letters
for i in range(1,upper_letter_choice+1):
    password_list.append(upper_letters[random.randint(0,len(upper_letters))-1])

# Add lower letters
for i in range(1,lower_letter_choice+1):
    password_list.append(lower_letters[random.randint(0,len(lower_letters)-1)])

# Add numbers
for i in range(1,numbers_choice+1):
    password_list.append(numbers[random.randint(0,len(numbers)-1)])

# Add symbols
for i in range(1,symbol_choice+1):
    password_list+=symbols[random.randint(0,len(symbols)-1)]

# shuffle element from list
random.shuffle(password_list)

# Copy password_list into clipboard
random.shuffle(password_list)
pyperclip.copy(password_list)
print("Successfully copid password_list into your clipboard")
