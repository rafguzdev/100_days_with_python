import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
let = int(input('How many letters: '))
num = int(input('How many numbers: '))
sym = int(input('How many symbols: '))
password = []

print(random.choice(letters))

for _ in range(let):
    password.append(random.choice(letters))
for _ in range(num):
    password.append(random.choice(numbers))
for _ in range(sym):
    password.append(random.choice(symbols))
random.shuffle(password)
password = ''.join(password)
print(password)