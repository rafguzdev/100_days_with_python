# Task 1 - add two digit
num = input('Type some 2 digit num: ')
num1 = int(num[0])
num2 = int(num[1])
sum = num1 + num2
print(sum)

# Task 2 - BMI - type, round
weight = int(input('Type weigth (kg): '))
height = float(input('Type height (m): '))
BMI = weight / ( height**2 )
BMI = round(BMI, 2)
print(BMI)

# Task 3 - Your life in weeks
age = int(input('Type your age: '))
days = ( 90 - age ) * 365
weeks = ( 90 - age ) * 52
months = ( 90 - age ) * 12
print(f'You have {days} days, {weeks} weeks and {months} months left.')

# Task 4 - Tip calculator 
print('Welcome to the tip calculator')
bill = float(input('What was the total bill?: $'))
tip = int(input('What percentage tip would you like to give? 10, 12 or 15?: '))
split = int(input('How many people to split the bill?: '))
pay = ( bill * tip / 100 + bill ) / split
pay = '{:.2f}'.format(pay)
print(f'Each person shoult pay: ${pay}')