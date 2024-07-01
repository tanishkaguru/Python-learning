#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
let= int(input("How many letters would you like in your password?\n")) 
sym = int(input(f"How many symbols would you like?\n"))
num = int(input(f"How many numbers would you like?\n"))

pas=""

for i in range(let):
    ind = random.randint(0, 51)
    pas += f"{letters[ind]}"
for i in range(sym):
    ind = random.randint(0, 8)
    pas += f"{symbols[ind]}"
for i in range(num):
    ind = random.randint(0, 9)
    pas += f"{numbers[ind]}"
pas=list(pas)
random.shuffle(pas)
pas="".join(pas)

print(f"Your password is: {pas}")