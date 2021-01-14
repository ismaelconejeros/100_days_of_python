from data import MENU

front = f'''
    ________________________________
   |      COFFEE MACHINE ☕        |
    |                              |
    | What would you like to have? |
    |                              |
    |  (1) Espresso (${MENU['espresso']['cost']})         |
    |  (2) Latte    (${MENU['latte']['cost']})         |
    |  (3) Cappuccino (${MENU['cappuccino']['cost']})       |
    |                              |
    |  (9) Tank Report             |
    |  (0) Turn off                |
    |______________________________|
    '''

head = '''
    ________________________________
   |      COFFEE MACHINE ☕        |
   '''