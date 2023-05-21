#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

setofletters = []
setofsymbols = []
setofnumbers = []
for i in range(nr_letters):
    random_index = random.randint(0,len(letters)-1)
    setofletters.append(letters[random_index])
for i in range(nr_symbols):
    random_index = random.randint(0,len(symbols)-1)
    setofsymbols.append(symbols[random_index])
for i in range(nr_numbers):
    random_index = random.randint(0,len(numbers)-1)
    setofnumbers.append(numbers[random_index])


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print(setofletters + setofsymbols + setofnumbers)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
one_list = setofletters + setofsymbols + setofnumbers
random.shuffle(one_list)
print(one_list)
password = ""
for item in one_list:
    password+=item
print(f"Your password is: {password}")
