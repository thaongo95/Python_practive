from frenchdeck import FrenchDeck
from random import choice

cards = FrenchDeck()

def three_cards_sum(three_cards):
	sum = 0
	for _card in three_cards:
		if _card in list("JQKA"):
			pass
		else:
			sum += int(_card)
	return sum%10;

def rank_score(rank):
	if rank == 'J': rank = 11
	elif rank == 'Q': rank  = 12
	elif rank == 'K': rank = 13
	elif rank == 'A': rank = 14
	else: rank= int(rank)
	return rank

def rank_index(card):
	rank_suit = dict(spides=3, hearts=2, diamonds=1, clubs=0)
	score = rank_score(card.rank)*4 + rank_suit[card.suit]
	return score


def isAAA(ranks):
	if ranks[0]==ranks[1]==ranks[2]:
		return True

def isABC(ranks):
	for i in range(len(ranks)):
		ranks[i] = rank_score(ranks[i])
	ranks = sorted(ranks)
	if ranks[2]-ranks[1]==1 and ranks[1]-ranks[0]==1:
		return True

while(True):
	three_cards = []
	big_card = cards[0]
	for i in range(3):
		while choice(cards) not in three_cards:
			card = choice(cards)
			break
		if rank_index(card) > rank_index(big_card):
			big_card = card
		print(card)
		three_cards.append(card.rank)
	print(f"sum of three cards is {three_cards_sum(three_cards)}")
	print(f"is this a AAA : {isAAA(three_cards)}")
	print(f"is this a ABC : {isABC(three_cards)}")
	print(f"biggest card in three one is : {big_card.rank} {big_card.suit}")
	q = input("Continue or not?")
	if q=='q':
		break
