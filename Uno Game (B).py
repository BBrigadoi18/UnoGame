# Bridget Brigadoi and Abby Thompson
# Math Modeling - Dr. McCullough

# This program simulates an number of uno games where one player is playing strategy and the other is playing normally/randomly
# Strategy: Player 1 will lay down number card first if applicable 

import random 

# Stack of cards
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
                    85: ("Wild", "Red"), 86: ("Wild", "Blue"), 87: ("Wild", "Green"), 88: ("Wild", "Yellow"), 89: ("Draw 4", "Red"), 90: ("Draw 4", "Blue"),
                    91: ("Draw 4", "Green"), 92: ("Draw 4", "Yellow"), 93: ("Skip", "Yellow"), 94: ("Skip", "Yellow"), 95: ("Skip", "Red"), 96: ("Skip", "Red"), 
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
    for n in range(len(player1_hand)):
        PLAYER_CARD = uno_cards_dict[player1_hand[n]] 
        if PLAYER_CARD[0] == uno_cards_dict[discard_pile_card][0]: 
            valid_color_cards.append(player1_hand[n])
        elif PLAYER_CARD[1] == uno_cards_dict[discard_pile_card][1]:
            valid_number_cards.append(player1_hand[n])


    for n in valid_number_cards:
        valid_color_cards.append(n)
    
    return valid_color_cards

# Player 2 is playing randomly - no strategy
def check_player2_hand(discard_pile_card, player2_hand):
    valid_cards = []
    for n in range(len(player2_hand)):
        
        PLAYER_CARD = uno_cards_dict[player2_hand[n]] 
        
        if PLAYER_CARD[1] == uno_cards_dict[discard_pile_card][1] or PLAYER_CARD[0] == uno_cards_dict[discard_pile_card][0]: 
            valid_cards.append(player2_hand[n])
    return valid_cards
    
# Draw from the deck if player does not have any valid cards 
def draw_card(draw_deck, player_hand):
    player_hand.append(draw_deck[0])
    draw_deck.remove(draw_deck[0])
    return draw_deck, player_hand

# Player lays down valid card in discard pile 
def lay_down_card(valid_player_hand, discard_pile, player_hand, draw_deck):
    try:
        card = valid_player_hand[0]
        discard_pile.append(card)
        player_hand.remove(card)
    except:
        draw_deck, player_hand = draw_card(draw_deck, player_hand)

    return discard_pile, player_hand

# Make the discard pile the new draw deck when draw deck is empty
def replenish_draw_deck(draw_deck, discard_pile):
   top_card = discard_pile[-1]
   discard_pile.remove(top_card)
   draw_deck = shuffle_cards(discard_pile)
   discard_pile = []
   discard_pile.append(top_card)

   return draw_deck, discard_pile


# Simulates player turn  
def player_turn(action, discard_pile, player_hand, draw_deck, player):
    top_card = discard_pile[-1]
    if action == True:
        if uno_cards_dict[top_card][0] == "Skip":
            action = False
            return action, discard_pile, player_hand, draw_deck
        elif uno_cards_dict[top_card][0] == "Draw 2":

            for n in range(0,2):
                if len(draw_deck) == 0: 
                    draw_deck, discard_pile = replenish_draw_deck(draw_deck, discard_pile)
                draw_deck, player_hand = draw_card(draw_deck, player_hand)
        
            action = False
            return action, discard_pile, player_hand, draw_deck
        
        elif uno_cards_dict[top_card][0] == "Draw 4":

            for n in range(0,4):
                if len(draw_deck) == 0: 
                    draw_deck, discard_pile = replenish_draw_deck(draw_deck, discard_pile)
                draw_deck, player_hand = draw_card(draw_deck, player_hand)
            action = False
            return action, discard_pile, player_hand, draw_deck
        
    player_options = []
    if player == 1:
        player_options = check_player1_hand(discard_pile[-1], player_hand)
    else:
        player_options = check_player2_hand(discard_pile[-1], player_hand)

    discard_pile, player_hand = lay_down_card(player_options, discard_pile, player_hand, draw_deck)
    if len(player_options) == 0:
        action = False
    else: 
        action = True
    return action, discard_pile, player_hand, draw_deck
 
trial_size = 1000
player1_wins = 0 
player2_wins = 0

for n in range(trial_size):


    card_list = list(range(1,101)) 

    player1_hand, player2_hand = distribute_cards(card_list)


    # Shuffle the main deck - becomes draw deck  
    draw_deck = shuffle_cards(card_list)

    # Let us start the game 
    discard_pile = []
    discard_pile.append(draw_deck[0])


    action = True 
    while True:
        # Reset draw pile from shuffle discard pile when draw deck is empty 
        if len(draw_deck) == 0: 
            draw_deck, discard_pile = replenish_draw_deck(draw_deck, discard_pile)

        action, discard_pile, player1_hand, draw_deck = player_turn(action, discard_pile, player1_hand, draw_deck, 1)

        if len(player1_hand) == 0:
            player1_wins += 1
            break 

        if len(draw_deck) == 0: 
            draw_deck, discard_pile = replenish_draw_deck(draw_deck, discard_pile)

        action, discard_pile, player2_hand, draw_deck = player_turn(action, discard_pile, player2_hand, draw_deck, 2)    

        if len(player2_hand) == 0:
            player2_wins += 1
            break 
probability_player1 = player1_wins/trial_size
probability_player2 = player2_wins/trial_size

print("Probability of Player 1 (Strategy: Number) winning: " + str(probability_player1))
print("Probability of Player 2 (Random): " + str(probability_player2))
