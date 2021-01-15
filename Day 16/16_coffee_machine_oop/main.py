from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from replit import clear

machine = CoffeeMaker()
wallet = MoneyMachine()
menu = Menu()

machine_on = True
while machine_on:
    clear()
    option = input('What do you want to do?\n(1) - Buy a coffee\n(2) - Print Report\n(3) - Turn off machine\n You option is: ')
    if option == '1':
        clear()
        coffee_option = input('What coffee do you want?\n(1) - Espresso\n(2) - Latte\n(3) - Cappuccino\n You option is: ')
        if coffee_option == '1':
            coffee = 'espresso'
        elif coffee_option == '2':
            coffee = 'latte'
        elif coffee_option == '3':
            coffee = 'cappuccino'
        
        if machine.is_resource_sufficient(menu.find_drink(coffee)):
            if wallet.make_payment(menu.find_drink(coffee).cost):
                machine.make_coffee(menu.find_drink(coffee))
            else:
                print('not enough money')
        else: 
            print('There is not enough resources in the tank.')
        go_back = input('\nPress enter to go back...)')
    elif option == '2':
        clear()
        machine.report()
        go_back = input('\nPress enter to go back...)')
    elif option == '3':
        machine_on = False
