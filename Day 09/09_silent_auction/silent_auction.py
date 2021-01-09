from replit import clear
from art import *


def add_auctioner(name, bid):
	auctioners[name] = bid

def auction_winner(auction_list):
	winner_name_list = []
	winner_bid_list = []
	for auctioner in auctioners:
		winner_name_list.append(name)
		winner_bid_list.append(auctioners[name])
	winner_bid = max(winner_bid_list)
	winner_name = winner_name_list[winner_bid_list.index(winner_bid)-1]
	print(f'the winner is {winner_name} with a bid of: ${winner_bid}')
	

auctioners = {}

auction_on = True
while auction_on:
	print(logo)
	name = input('What is your name?\n')
	bid = int(input('What is your bid price\n'))
	
	add_auctioner(name, bid)

	again = input('Is there any other auctioner?\n (Y or N)').lower()

	if again == 'y':
		clear()
	else:
		clear()
		print(logo)
		auction_winner(auctioners)
		auction_on = False