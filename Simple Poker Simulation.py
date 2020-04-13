import random
import sys

# Creates Deck of cards
spades = ['S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA']
clubs = ['C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK', 'CA']
hearts = ['H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'HA']
diamonds = ['D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'DA']

Deck = spades + clubs + hearts + diamonds

# Creates poker hand with five different cards from the Deck
i = 0
hand = []
while i <= 1:
    hand = hand + random.choices(Deck)
    i += 1
print('You were dealt {x}!'.format(x=hand))

# Creating the flop_deck and displaying the flop
flop_deck = sorted(list(set(Deck).difference(set(hand))))  # creates new list with hand values removed from Deck
flop_count = 0
flop = []
while flop_count <= 2:
    flop = flop + random.choices(flop_deck)
    flop_count += 1
print('The flop comes {cards}'.format(cards=flop))

# Creating the turn deck and displaying the turn card
turn_deck = list(set(flop_deck).difference(set(flop)))
turn = random.choices(turn_deck)
print('The turn card is {card}'.format(card=turn))

# Creating the river deck and displaying the river card
river_deck = list(set(turn_deck).difference(set(turn)))
river = random.choices(river_deck)
print('The river card is {card}'.format(card = river))