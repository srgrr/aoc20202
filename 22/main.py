import sys
from collections import deque
from functools import reduce

# Parse input
decks = []

with open(sys.argv[1]) as f:
  for _ in range(2):
    deck = []
    line = f.readline().strip()
    line = f.readline().strip()
    while line:
      deck.append(int(line))
      line = f.readline().strip()
    decks.append(deque(deck))


# Part 1
def top_cards(decks):
  return decks[0].popleft(), decks[1].popleft()


def print_winner(decks):
  winner_deck = decks[0] or decks[1]
  print(sum([(i + 1) * v for i, v in enumerate(reversed(winner_deck))]))


def win(decks, player, t1, t2):
  if player:
    t1, t2 = t2, t1
  decks[player].append(t1)
  decks[player].append(t2)


p1_decks = [x.copy() for x in decks]

while all(p1_decks):
  t1, t2 = top_cards(p1_decks)
  win(p1_decks, t1 <= t2, t1, t2)

print_winner(p1_decks)

# Part 2
def game(decks):
  mem = set()
  while all(decks):
    current_state = (tuple(decks[0]), tuple(decks[1]))
    t1, t2 = top_cards(decks)
    if current_state in mem:
      win(decks, 0, t1, t2)
      return 0
    mem.add(current_state)
    dqt = list(zip(decks, [t1, t2]))
    if all(t <= len(dq) for dq, t in dqt):
      win(decks, game([deque(list(dq)[:t]) for dq, t in dqt]), t1, t2)
    else:
      win(decks, t1 <= t2, t1, t2)
  return 0 if decks[0] else 1

game(decks)

print_winner(decks)