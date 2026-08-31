print("welcome to the password generator\n")

import random
letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
symbol = ["~","`","!","@","#","$","%","^","&","*","(",")","_","-","=","+"]  
number = ["1","2","3","4","5","6","7","8","9","0"]

no_letter = int(input("How many letter would you like in your password:\n"))
no_symbol = int(input("How many symbol would you like:\n"))
no_number = int(input("How many number would you like:\n"))

password = []

for char in range(0,no_letter):
    password.append(random.choice(letter))

for char in range(0,no_symbol):
    password.append(random.choice(symbol))

for char in range(0,no_number):
    password.append(random.choice(number))

random.shuffle(password)

final_pass = ""

for char in password:
    final_pass += char

print(f"Your password is: {final_pass}")
