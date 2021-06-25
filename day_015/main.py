# Coffe machine
import menu as data

menu = data.MENU
resources = data.resources
money = 0

def check_resources(product):
    ingredients = menu[product]['ingredients']
    for ingredient, value in ingredients.items():
        if resources[ingredient] < value:
            return f'Sorry there is not enough {ingredient}'
    return True
    
while True:

    while True:
        task = input('What would you like? (espresso/latte/cappucino): ')
        if task == 'espresso' or task == 'latte' or task == 'cappucino' or task == 'report':
            break
        else:
            print("I don't understand...")

    if task == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffe: {resources["coffee"]}g')
        print(f'Money: {money}zł')
    else:
        res = check_resources(task)
        if type(res) == bool:
            pass
        else:
            print(res)
