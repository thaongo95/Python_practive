import collections


class FrenchDeck:
	Card = collections.namedtuple("Card", ["rank","suit"])
	ranks = [str(i) for i in range(2,11)] + list("JQKA")
	suits = "spides diamonds clubs hearts".split()
	
	def __init__(self):
		self._cards = [self.Card(rank, suit) for rank in self.ranks for suit in self.suits]
	
	def __len__(self):
		return len(self._cards)
	
	def __getitem__(self, pos):
		return self._cards[pos]
