'''
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value. 
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair. 
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

Issue occuring when both have one pair - fix by checking for highest pair value(Done: 20/8/17)
Improve by adding value of max occuring for other hands
'''

import math 
import time 
start = time.time()

def read_data(path):
	file = open(path,mode='r').read() #read converts the read object into a string
	# print(str(file))
	all_hands = list(file.split('\n')) 

	#Preprocesssing player hands in every iteration
	player_1 = [[] for i in xrange(len(all_hands))]
	player_2 = [[] for i in xrange(len(all_hands))]
	for index,entry in enumerate(all_hands):
		temp = list(entry.split(" "))
		player_1[index] = temp[:5]
		player_2[index] = temp[-5:]

	return player_1,player_2

def value_suits(player_cards):
	card_values = []
	card_suits = []
	dict_values = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10}
	for card in player_cards:
		try:
			card_values.append(int(card[0]))
		except:
			card_values.append(dict_values[card[0]])
		card_suits.append(card[1])

	return card_values,card_suits

def is_consecutive(l):
    setl = set(l)
    return len(l) == len(setl) and setl == set(range(min(l), max(l)+1))

def common_kind(values):
	unique_values = set(values)
	common_pairs = []
	for unique_value in unique_values:
		common_pairs.append(values.count(unique_value))
	return sorted(common_pairs,reverse=True)

def most_common(lst):
    return max(set(lst), key=lst.count)

def royal_flush(card_values,card_suits):
	return set(card_values) == set(range(10,15)) and len(set(card_suits)) == 1

def straight_flush(card_values,card_suits):
	return is_consecutive(card_values) and len(set(card_suits)) == 1

def four_of_a_kind(card_values,card_suits):
	return len(set(card_values)) == 2 and common_kind(card_values) == [4,1]

def full_house(card_values,card_suits):
	return len(set(card_values)) == 2 and common_kind(card_values) == [3,2]

def flush(card_values,card_suits):
	return len(set(card_suits)) == 1
		
def straight(card_values,card_suits):
	return is_consecutive(card_values)

def three_of_a_kind(card_values,card_suits):
	return len(set(card_values)) == 3 and common_kind(card_values) == [3,1,1]

def two_pairs(card_values,card_suits):
	return len(set(card_values)) == 3 and common_kind(card_values) == [2,2,1]

def one_pair(card_values,card_suits):
	return len(set(card_values)) == 4

def high_card(card_values,card_suits):
	return max(card_values)

def hand_type(hand):
	player_values,player_suits = value_suits(hand)
	# print(common_kind(player_values))
	if royal_flush(player_values,player_suits):
		return 23
	elif straight_flush(player_values,player_suits):
		return 22 # + max(player_values)
	elif four_of_a_kind(player_values,player_suits):
		return 21 # + most_common(player_values)
	elif full_house(player_values,player_suits):
		return 20 # + most_common(player_values)
	elif flush(player_values,player_suits):
		return 19
	elif straight(player_values,player_suits):
		return 18 # + max(player_values)
	elif three_of_a_kind(player_values,player_suits):
		return 17 # + most_common(player_values)
	elif two_pairs(player_values,player_suits):
		return 16  # + 
	elif one_pair(player_values,player_suits):
		return 15
	else:
		return high_card(player_values,player_suits)

def main():
	result_count = 0
	test_set = set()
	player_A,player_B  = read_data('p054_poker.txt') #Get player moves
	
	for move in xrange(0,len(player_A)-1):

		if hand_type(player_A[move]) > hand_type(player_B[move]):
			result_count += 1
			test_set.add(move)
		
		if hand_type(player_A[move]) == hand_type(player_B[move]):
			value_1,_ = value_suits(player_A[move])
			value_2,_ = value_suits(player_B[move])
			if most_common(value_1) > most_common(value_2):
				result_count += 1

	return result_count #,map(str,test_set)
	
elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #0.1s

'''
_,test_hands = main()
test_hands = set(test_hands)

file_winning_hands = open('Winning_hands.txt',mode='r').read() 
winning_hands = set(file_winning_hands.split('\n')) 
winning_hands.remove('')



common_elements = winning_hands.intersection(test_hands)
print(len(common_elements))
missing_elements = winning_hands.difference(test_hands)
print(missing_elements)
wrong_elements = test_hands.difference(winning_hands)
print(wrong_elements)
# print(len(winning_hands))
'''