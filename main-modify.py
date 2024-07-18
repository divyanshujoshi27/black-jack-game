import random

class DiamondCards:
    def __init__(self):
        self.cards = {
            'A': """
.------.
|A ♦  |
| ♦  ♦ |
|  ♦  |
| ♦  ♦ |
`------'
""",
            '2': """
.------.
|2 ♦  |
|     |
|  ♦  |
|     |
`------'
""",
            '3': """
.------.
|3 ♦  |
|     |
| ♦ ♦ |
|  ♦  |
`------'
""",
            '4': """
.------.
|4 ♦  |
| ♦ ♦ |
|     |
| ♦ ♦ |
`------'
""",
            '5': """
.------.
|5 ♦  |
| ♦ ♦ |
|  ♦  |
| ♦ ♦ |
`------'
""",
            '6': """
.------.
|6 ♦  |
| ♦ ♦ |
| ♦ ♦ |
| ♦ ♦ |
`------'
""",
            '7': """
.------.
|7 ♦  |
| ♦ ♦ |
|♦ ♦ ♦|
| ♦ ♦ |
`------'
""",
            '8': """
.------.
|8 ♦  |
| ♦ ♦ |
|♦ ♦ ♦|
| ♦ ♦ |
`------'
""",
            '9': """
.------.
|9 ♦  |
|♦ ♦ ♦|
|♦ ♦ ♦|
| ♦ ♦ |
`------'
""",
            '10': """
.------.
|10♦  |
|♦ ♦ ♦|
|♦ ♦ ♦|
|♦ ♦ ♦|
`------'
""",
            'J': """
.------.
|J ♦  |
|     |
|  J  |
|     |
`------'
""",
            'Q': """
.------.
|Q ♦  |
|     |
|  Q  |
|     |
`------'
""",
            'K': """
.------.
|K ♦  |
|     |
|  K  |
|     |
`------'
"""
        }

    def get_card(self, rank):
        return self.cards.get(rank, "Card not found")


diamond_cards = DiamondCards()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def random_list(card):
    """Selects a random card from the given list"""
    choice_my = random.choice(card)
    card_representation = str(choice_my)
    if choice_my == 11:
        card_representation = 'A'
    elif choice_my == 10:
        face_cards = ['10', 'J', 'Q', 'K']
        card_representation = random.choice(face_cards)
    print(diamond_cards.get_card(card_representation))
    return choice_my


def add_list(lst):
    add_no = sum(lst)
    return add_no


def winner(my_total, com_total):
    if my_total > com_total and my_total <= 21:
        return "you win"
    elif my_total < com_total and com_total <= 21:
        return "you lose"
    elif my_total == com_total and my_total <= 21 and com_total <= 21:
        return "draw"
    else:
        if my_total > 21:
            return "you lose"
        elif com_total > 21:
            return "you win"
    return "game continues"


def adjust_for_ace(deck):
    """Adjusts Aces from 11 to 1 if total exceeds 21"""
    while sum(deck) > 21 and 11 in deck:
        deck[deck.index(11)] = 1
    return deck


my_deck = cards.copy()
com_deck = cards.copy()

score_my = 0
score_com = 0

my_random = []
com_random = []

# Initial dealing of cards
while score_my < 2:
    my_random.append(random_list(my_deck))
    com_random.append(random_list(com_deck))
    score_my += 1

print(my_random)  # list of my deck
print(com_random)  # list of com deck

total_my = add_list(my_random)
total_com = add_list(com_random)

# Adjust for Aces initially dealt
my_random = adjust_for_ace(my_random)
com_random = adjust_for_ace(com_random)

total_my = add_list(my_random)
total_com = add_list(com_random)

# Main game loop
while total_com < 22 and total_my < 22:
    print("Do you want to add a card?")
    choice = input("yes or no: ")
    if choice == "yes":
        my_random.append(random_list(my_deck))
        com_random.append(random_list(com_deck))
        my_random = adjust_for_ace(my_random)
        com_random = adjust_for_ace(com_random)
        total_my = add_list(my_random)
        total_com = add_list(com_random)
        print(f"Your total is {total_my}, Computer's total is {total_com}")
    else:
        break

print(winner(total_my, total_com))

print(my_random)  # list of my deck
print(com_random)  # list of com deck
