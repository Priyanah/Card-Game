# 1. Create Card class
# 2. Choose Suit of class(KING, QUEEN, ACE, etc) Rank of cards, and then value of cards

import random

suits = ('Hearts', 'Diamond', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


three_of_clubs = Card("Clubs", "Three")
print(three_of_clubs)
val = three_of_clubs.suit
print(val)

two_hearts = Card("Hearts", "Two")
print(two_hearts)
print(two_hearts.value)

bool = two_hearts.value < three_of_clubs.value  # comparison between two cards
print(bool)


class Deck:
    def __init__(self):
        self.all_cards = []  # empty array contains all 52 cards

        for suit in suits:  # Each card
            for rank in ranks:  # Each card rank
                # Create Card Object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):  # will shuffle only one card from the whole deck
        return self.all_cards.pop()


new_deck = Deck()
new_deck.shuffle()
mycard = new_deck.deal_one()
print(mycard)

len(new_deck.all_cards)

new_deck = Deck()
first_card = new_deck.all_cards[51]  # here number in brackets depicts card in deck
print(first_card)

for card_object in new_deck.all_cards:
    print(card_object)

new_deck.shuffle()
print(new_deck.all_cards[0])


# Player Class


class Player:

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of Multiple Card objects
            self.all_cards.extend(
                new_cards)            # here append can't be used because it will make a list in list (['1','2','3',['4','5'],'7']) so "extend" is used.
        else:
            # For a Single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


new_player = Player('Priyansh')
print(new_player)

new_player.add_cards(mycard)
print(mycard)

print(new_player)

print(new_player.all_cards[0])

new_player.add_cards([mycard, mycard, mycard])
print(new_player)

new_player.remove_one()
print(new_player)

# Main Logic

# defining Players
player_one = Player("Player One: ")
player_two = Player("Player Two: ")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
print(len(player_one.all_cards))

game_on = True

round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two Wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards! Player One Wins!")
        game_on = False
        break

        # Start a New Round

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    in_game = True

    while in_game:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            in_game = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            in_game = False

        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:   #lesser the number longer the game
                print("Player One enable to declare War! ")
                print("Player Two WINS! ")
                game_on = False
                break

            if len(player_two.all_cards) < 5:   #lesser the number longer the game
                print("Player Two enable to declare War! ")
                print("Player One WINS! ")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
