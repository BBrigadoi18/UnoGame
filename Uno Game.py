

# Similulating an Uno Game 

# Stack of cards

import random 


uno_cards_dict = {1: ("0", "Red"), 2: ("1", "Red"), 3: ("2", "Red"), 4: ("3", "Red"), 5: ("4", "Red"), 6: ("5", "Red"), 7: ("6", "Red"), 8: ("7", "Red"), 9: ("8", "Red"), 
                    10: ("9", "Red"), 11: ("1", "Red"), 12: ("2", "Red"), 13: ("3", "Red"), 14: ("4", "Red"), 15: ("5", "Red"),  16: ("6", "Red"), 17: ("7", "Red"), 18: ("8", "Red"), 
                    19: ("9", "Red"), 20: ("0", "Blue"), 21: ("1", "Blue"), 22: ("2", "Blue"), 23: ("3", "Blue"), 24: ("4", "Blue"), 25: ("5", "Blue"), 26: ("6", "Blue"), 
                    27: ("7", "Blue"), 28: ("8", "Blue"), 29: ("9", "Blue"), 30: ("1", "Blue"), 31: ("2", "Blue"), 32: ("3", "Blue"), 33: ("4", "Blue"), 34: ("5", "Blue"), 
                    35: ("6", "Blue"), 36:("7", "Blue"), 37: ("8", "Blue"), 38:("9", "Blue"), 39: ("0", "Green"), 40: ("1", "Green"), 41: ("2", "Green"), 42: ("3", "Green"), 
                    43: ("4", "Green"), 44: ("5", "Green"), 45: ("6", "Green"), 46: ("7", "Green"), 47: ("8", "Green"), 48: ("9", "Green"), 49: ("1", "Green"), 
                    50: ("2", "Green"), 51: ("3", "Green"), 52: ("4", "Green"), 53: ("5", "Green"), 54: ("6", "Green"), 55: ("7", "Green"), 56: ("8", "Green"), 57: ("9", "Green"),
                    58: ("0", "Yellow"), 59: ("1", "Yellow"), 60: ("2", "Yellow"), 61: ("3", "Yellow"), 62: ("4", "Yellow"), 63: ("5", "Yellow"), 64: ("6", "Yellow"), 
                    65: ("7", "Yellow"), 66: ("8", "Yellow"), 67: ("9", "Yellow"), 68:("1", "Yellow"), 69: ("2", "Yellow"), 70: ("3", "Yellow"), 71: ("4", "Yellow"), 
                    72: ("5", "Yellow"), 73: ("6", "Yellow"), 74: ("7", "Yellow"), 75: ("8", "Yellow"), 76: ("9", "Yellow"), 77: ("Draw 2", "Red"), 78: ("Draw 2", "Red"),
                    79: ("Draw 2", "Blue"), 80: ("Draw 2", "Blue"), 81: ("Draw 2", "Green"), 82: ("Draw 2", "Green"),  83: ("Draw 2", "Yellow"), 84: ("Draw 2", "Yellow"), 
                    85: ("Wild", "Black"), 86: ("Wild", "Black"), 87: ("Wild", "Black"), 88: ("Wild", "Black"), 89: ("Draw 4", "Black"), 90: ("Draw 4", "Black"),
                    91: ("Draw 4", "Black"), 92: ("Draw 4", "Black"), 93: ("Skip", "Yellow"), 94: ("Skip", "Yellow"), 95: ("Skip", "Red"), 96: ("Skip", "Red"), 
                    97: ("Skip", "Green"), 98: ("Skip", "Green"), 99: ("Skip", "Blue"), 100: ("Skip", "Blue")}

# Generate random cards within range of cards; confirm that there are no duplicates
def distribute_cards(card_list):

    player1_hand = []
    player2_hand = []

    player1_hand = random.sample((card_list), 7)

    for n in player1_hand:
        card_list.remove(n)

    player2_hand = random.sample((card_list), 7)

    for n in player2_hand:
        card_list.remove(n)

    return player1_hand, player2_hand

# Shuffle the deck 
def shuffle_cards(card_list):
    random.shuffle(card_list)
    return card_list

# Player 1 is playing strategy - color first 
def check_player1_hand(discard_pile_card, player1_hand):
    valid_color_cards = []
    valid_number_cards = []
    for n in player1_hand:
        if player1_hand[n][1] == uno_cards_dict[discard_pile_card][1]: 
            valid_color_cards.append(n)
        elif player1_hand[n][0] == uno_cards_dict[discard_pile_card][0]:
            valid_number_cards.append(n)
    return valid_color_cards, valid_number_cards

# Player 2 is playing randomly - no strategy
def check_player2_hand(discard_pile_card, player2_hand):
    valid_cards = []
    for n in player2_hand:
        if player2_hand[n][1] == uno_cards_dict[discard_pile_card][1] or player2_hand[n][0] == uno_cards_dict[discard_pile_card][0]:
            valid_cards.append(n)
    return valid_cards

# Function to check if player 1 can lay down a color; if not, checks for number
def player1_options(color_list, number_list):
    if len(color_list) > 0:
        return color_list
    elif len(number_list) > 0:
        return number_list
    else:
        return []    # They have no valid cards to put down 
    
# Draw from the deck if player does not have any valid cards 
def draw_card(draw_deck, player_hand):
    player_hand.append(draw_deck[0])
    draw_deck.remove(draw_deck[0])
    return player_hand, draw_deck

# Player lays down valid card in discard pile 
def lay_down_card(valid_player_hand, discard_pile, player_hand):
    card = random.choice(valid_player_hand)
    discard_pile.append(card)
    player_hand.remove(card)
    return discard_pile, player_hand




    

   


# print(uno_cards_dict[97][1])
# For now, no special cards
card_list = list(range(1,77))

player1, player2 = distribute_cards(card_list)


# Shuffle the main deck - becomes draw deck  
draw_deck = shuffle_cards(card_list)

discard_pile = []
discard_pile.append(draw_deck[0])
counter = 0
# Play until draw deck is out then shuffle

while len(player1) > 0 or len(player2) > 0:
    # Reset draw pile from shuffle discard pile
    if len(draw_deck) == 0: 
        random.shuffle(discard_pile)
        draw_deck = discard_pile
        discard_pile = [] 
    




    




















   

