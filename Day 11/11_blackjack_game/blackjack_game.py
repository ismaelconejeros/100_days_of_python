import random
from replit import clear
from art import logo

card_deck = ['A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
             'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
             'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣',
             'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']

card_value = {'A♥': 11, '2♥': 2, '3♥': 3, '4♥': 4, '5♥': 5, '6♥': 6, '7♥': 7, '8♥': 8, '9♥': 9, '10♥': 10, 'J♥': 10, 'Q♥': 10, 'K♥': 10,
              'A♦': 11, '2♦': 2, '3♦': 3, '4♦': 4, '5♦': 5, '6♦': 6, '7♦': 7, '8♦': 8, '9♦': 9, '10♦': 10, 'J♦': 10, 'Q♦': 10, 'K♦': 10,
              'A♣': 11, '2♣': 2, '3♣': 3, '4♣': 4, '5♣': 5, '6♣': 6, '7♣': 7, '8♣': 8, '9♣': 9, '10♣': 10, 'J♣': 10, 'Q♣': 10, 'K♣': 10,
              'A♠': 11, '2♠': 2, '3♠': 3, '4♠': 4, '5♠': 5, '6♠': 6, '7♠': 7, '8♠': 8, '9♠': 9, '10♠': 10, 'J♠': 10, 'Q♠': 10, 'K♠': 10
              }

def info():
    clear()
    print(logo)
    print(f'The cards of the dealer are: {dealer_cards} and the value is {dealer_value}')
    print(f'The cards of the player are: {player_cards} and the value is {player_value}')

def new_card_init():
    global player_value, dealer_value
    card = random.choice(card_deck)
    player_cards.append(card)
    player_value += card_value[card]
    shoe.remove(card)
    card = random.choice(card_deck)
    dealer_cards.append(card)
    dealer_value += card_value[card]
    shoe.remove(card)
    card = random.choice(card_deck)
    player_cards.append(card)
    if player_value > 10 and card_value[card] == 11:
        player_value += 1
    else:
        player_value += card_value[card]
    shoe.remove(card)

def player_turn():
    global player_value, dealer_value
    card = random.choice(card_deck)
    player_cards.append(card)
    if player_value > 10 and card_value[card] == 11:
        player_value += 1
    else:
        player_value += card_value[card]
    shoe.remove(card)

def dealer_turn():
    global dealer_value
    while dealer_value < 17:
        card = random.choice(card_deck)
        dealer_cards.append(card)
        dealer_value += card_value[card]

def check_win():
    global player_value, dealer_value, game_stage
    if game_stage == 1:
        if player_value == 21:
            print('\n *** PLAYER WINS ***\n')
            game_stage = 0
            again = input('Press ENTER to play again...')
        elif player_value > 21:
            print('*** DEALER WINS ***')
            game_stage = 0
            again = input('Press ENTER to play again...')
    else:
        if player_value == dealer_value:
            print('*** IT\'S A TIE ***')
            game_stage = 0
            again = input('Press ENTER to play again...')
        elif dealer_value > 21:
            print('*** PLAYER WINS ***')
            game_stage = 0
            again = input('Press ENTER to play again...')
        elif player_value > dealer_value:
            print('*** PLAYER WINS ***')
            game_stage = 0
            again = input('Press ENTER to play again...')
        elif player_value < dealer_value:
            print('*** DEALER WINS ***')
            game_stage = 0
            again = input('Press ENTER to play again...')


game_stage = 0
game_on = True

while game_on:
    while game_stage == 0: #INIT GAME
        player_cards = []
        player_value = 0
        dealer_cards = []
        dealer_value = 0
        shoe = card_deck * 6

        new_card_init()
        game_stage = 1

    while game_stage == 1: #PLAYER'S TURN
        info()
        check_win()
        if game_stage == 1:
            player_choose = input('Press "Y" to HIT and "N" to STAND: ').lower()
            if player_choose == 'y':
                player_turn()
            elif player_choose == 'n':
                game_stage = 2

    while game_stage == 2: #DEALER'S TURN
        dealer_turn()
        info()
        check_win()