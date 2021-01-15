from data import resources, MENU
from art import front, head
from replit import clear

def print_report():
    clear()
    print(head)
    print('The coffe machine tank is: ')
    print(f"Water: {water_tank} ml {(water_tank/resources['water'])*100:.2f}%")
    print(f"Milk: {milk_tank} ml {(milk_tank/resources['milk'])*100:.2f}% ")
    print(f"coffee: {coffee_tank} ml {(coffee_tank/resources['coffee'])*100:.2f}% ")
    print('The coffe machine wallet is: ')
    print(f'${wallet}.\n')
    print('The coffe machine log is: ')
    print(f'{history}\n')
    go_back = input('Press any key to go back.')

def check_req(coffee):
    if water_tank >= MENU[coffee]['ingredients']['water'] and milk_tank >= MENU[coffee]['ingredients']['milk'] and coffee_tank >= MENU[coffee]['ingredients']['coffee']:
        return True
    else:
        return False

def make_coffee(coffee):
    global water_tank, milk_tank, coffee_tank, wallet
    water_tank -= MENU[coffee]['ingredients']['water']
    milk_tank -= MENU[coffee]['ingredients']['milk']
    coffee_tank -= MENU[coffee]['ingredients']['coffee']
    wallet += MENU[coffee]['cost']
    history.append((coffee, MENU[coffee]['cost']))
    print(f'Thank you for stopping by, here is your {coffee}.\nHave a nice day\n')
    go_back = input('Press any key to go back.')

def insert_money(coffee):
    global wallet, status
    balance = 0
    while balance < MENU[coffee]['cost']:
        clear()
        print(head)
        print(f"The price is: ${MENU[coffee]['cost']}\n")
        print(f'You balance is: ${balance}.\n')
        coin = float(input('Please enter a coin:\n'))
        balance += coin
        wallet += balance
    clear()
    print(head)
    print(f'Ready for your {coffee}?\n')
    confirm = input('Press Y to confirm\nPress N to cancel\n').lower()
    if confirm == 'y':
        wallet -= (balance - MENU[coffee]['cost'])
        status = 1
        print(f"You have a refund of: ${balance - MENU[coffee]['cost']:.2f}")
    elif confirm == 'n':
        wallet -= balance
        print(f'You have a refund of: ${balance:.2f}')
        go_back = input('Press any key to go back.')

water_tank = resources['water']
milk_tank = resources['milk']
coffee_tank = resources['coffee']
wallet = 0
history = []

machine_on = True
while machine_on:
    clear()
    print(front)
    status = 0
    option = input('What would you like to do?\n')
    if option == '1':
        coffee_picked = 'espresso'
    elif option == '2':
        coffee_picked = 'latte'
    elif option == '3':
        coffee_picked = 'cappuccino'
    elif option == '9':
        print_report()
    elif option == '0':
        machine_on = False

    if option in ['1', '2', '3']:
        if check_req(coffee_picked):
            insert_money(coffee_picked)
            if status == 1:
                make_coffee(coffee_picked)
                status = 0
        else:
            print('There are no resources enough in the tank')
            go_back = input('Press any key to go back.')