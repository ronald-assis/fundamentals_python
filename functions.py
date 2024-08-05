import random

def sum_two(n):
    return n + 2


print(sum_two(5))

text = 'Ola mundo:wa'
key = 2

alphabets_lowerCase = 'abcdefghijklmnopqrstuvwxyz'
alphabets_upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cifraCharacter(c, seq, key):
    index = seq.index(c)
    new_index = index + key
    # Lidar com situação onde índice está à direita da seq
    while new_index >= len(seq):
        new_index -= len(seq)
    while new_index < 0:
        new_index += len(seq)

    return seq[new_index]

cifra = ''


for character in text:
    if character in alphabets_lowerCase:
        character_cifra = cifraCharacter(character, alphabets_lowerCase, key)
    elif character in alphabets_upperCase:
        character_cifra = cifraCharacter(character, alphabets_upperCase, key)
    else:
        character_cifra = character
    cifra += character_cifra

print(cifra)


def generateDeck(n_copy, joker = True, scrambled = True):
    deck = []

    suits = list('POEC')
    numbers = list('23456789JQKA') + ['10']

    for _ in range(n_copy):
        for suit in suits:
            for number in numbers:
                print(number, suit)
                card = number + suit
                deck.append(card)
        if joker:
            deck.extend(['JK1', 'JK2'])

    if scrambled:
        random.shuffle(deck)

    return deck


def show_deck(deck):
    print(f'Há {len(deck)} cartas')
    print(' | '.join(deck))


def distributingCards(deck, n_players=4, n_cards=5):
    players = {}

    for i in range(n_players):
        hand = []
        while len(hand) < n_cards:
            card = deck.pop(0)
            hand.append(card)
        name_player = f'Player {i+1}'
        players[name_player] = hand

    return players

def show_player_hands(players):
    for player, hands in players.items():
        print(f'ha {len(hands)} cartas no jogador {player}')
        for card in hands:
            print(f' -> {card}')


deck = generateDeck(1)


show_deck(deck)


players = distributingCards(deck)

show_player_hands(players)
print(players)





