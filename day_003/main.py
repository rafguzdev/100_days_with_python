# Task 1 - odd or even
num = int(input('Type a number: '))
if num % 2 == 0:
    print('even')
else:
    print('odd')

# Task 2 - BMI2.0
BMI = float(input('Type BMI: '))
if BMI < 18.5:
    print('underweight')
elif BMI < 25.0:
    print('normal weight')
elif BMI < 30:
    print('overweight')
elif BMI < 35:
    print('obese')
else:
    print('clinically obese')

# Task 3 - Leap Year
year = int(input('Witch year do you want to check?: '))
lap_year = False
if year % 4 == 0:
    lap_year = True
    if year % 100 == 0:
        lap_year = False
        if year % 400 == 0:
            lap_year = True
print(f'Leap Year - {lap_year}')

# Task 4 - Pizza order
size = input('What size pizza do you want? S, M, L: ')
add_peperoni = input('Do you want extra pepperoni y/n? ')
extra_cheese = input('Do you want extra cheese y/n? ')
price = 0
if size == 's':
    price = 15
elif size == 'm':
    price = 20
else:
    price = 25
if add_peperoni == 'y':
    if size == 's':
        price += 2
    else:
        price += 3
if extra_cheese == 'y':
    price += 1

print(f'${price}')

# Task 5 - Love calculator
name1 = input('Whai is your name? ')
name2 = input('Whai is their name? ')
name = name1 + name2
name.lower()
t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
true = t + r + u + e
l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')
love = l + o + v + e
num = str(true) + str(love)
num = int(num)
if num < 10 or num > 90:
    print(f'Your score is {num}, you go together like coke and mentos.')
elif num > 40 and num < 50:
    print(f'Your score is {num}, you are alrigth together.')
else:
    print(f'Your score is {num}.')

# Task 6 - Treasure Island
print('Welcome to Treasure Island')
if 'left' == input('left or right? ').lower():
    if 'wait' == input('swim or wait? ').lower():
        if 'yellow' == input('Whitch door? red/blue/yellow ').lower():
            print('You win')
        else:
            print('game over')
    else:
        print('game over')
else:
    print('game over')