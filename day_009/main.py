# Task 1 - grades
students_scores = {
    'Ada': 81,
    'Rafal': 28,
    'Jan': 99,
    'Jolanta': 100
}

students_grages = {}

for (key, value) in students_scores.items():
    if value > 91:
        students_grages[key] = 'Outstanding'
    elif value > 80:
        students_grages[key] = 'Good'
    else:
        students_grages[key] = 'Bad'

print(students_grages)

# Task 2
travel_log = [
    {
        'country': 'France',
        'visits': 12,
        'cities': ['Paris', 'Lille']
    }
] 

def add_new_country(country, visits, cities):
    travel_log.append({
        'country': country,
        'visits': visits,
        'cities': cities
    })

add_new_country("Russia", "2", ['Moscow'])
print(travel_log)

# Task 3 - Final list
import os
clear = lambda: os.system('cls')
myDict = {}
while True:
    name = input('Your name: ')
    bid = int(input('Your bid: '))
    myDict[name] = bid
    more = input('Are there any other bidders? Type "yes" or "no": ')
    if more == 'no':
        winner_name = ''
        winner_bid = 0
        for key, value in myDict.items():
            if value > winner_bid:
                winner_name = key
                winner_bid = value
        print(f'Winner is {winner_name} with {winner_bid}')
        break
    else:
        clear()