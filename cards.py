import random

class Card(object):
  def __init__(self, number=0, suit=0):
    self.number = number
    self.suit = suit

  def print_card(self):
    suits = {0:'JOKAH', 1:'S', 2:'D', 3:'H', 4:'C'}
    if self.number == 1:
      t = 'A'
    else:
      t = self.number
    print(str(t)+str(suits[self.suit]))

class Deck(object):
  def __init__(self):
    self.deck = []

  def shuffle(self):
    random.shuffle(self.deck)

  def destroy(self):
    del self.deck[:]

  def build(self):
    for j in range(4):
      for i in range(13):
        self.deck.append(Card(i, j+1))

  def get_len(self):
    return len(self.deck)

  def get_card(self, pos):  # pos = position in deck
    return self.deck[pos]

d = Deck()
d.build()
d.shuffle()
dl = d.get_len()

for i in range(1, dl):
  d.get_card(i).print_card()

d.destroy()
