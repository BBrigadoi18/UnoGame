

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
                      65: ("7", "Yellow"), 66: ("8", "Yellow"), 67: ("9", "Yellow"), 68:("1", "Yellow"), 69: ("2", "Yellow"),  70: ("3", "Yellow"), 71: ("4", "Yellow"), 
                      72: ("5", "Yellow"), 73: ("6", "Yellow"), 74: ("7", "Yellow"), 75: ("8", "Yellow"), 76: ("9", "Yellow"),77: ("Draw 2", "Red"), 78: ("Draw 2", "Red"),
                      79: ("Draw 2", "Blue"), 80: ("Draw 2", "Blue"), 81: ("Draw 2", "Green"), 82: ("Draw 2", "Green"),  83: ("Draw 2", "Yellow"), 84: ("Draw 2", "Yellow"), 
                      85: ("Wild", "Black"), 86: ("Wild", "Black"), 87: ("Wild", "Black"), 88: ("Wild", "Black"), 89: ("Draw 4", "Black"), 90: ("Draw 4", "Black"),
                      91: ("Draw 4", "Black"), 92: ("Draw 4", "Black"), 93: ("Skip", "Yellow"), 94: ("Skip", "Yellow"), 95: ("Skip", "Red"), 96: ("Skip", "Red"), 
                      97: ("Skip", "Green"), 98: ("Skip", "Green"), 99: ("Skip", "Blue"), 100: ("Skip", "Blue")}


card_list = []
for n in range(1,101):
    card_list.append(n)

# Generate random cards within range of cards; confirm that there are no duplicates  
player1_hand = random.sample(range(len(card_list)), 7)
print(player1_hand)

for n in player1_hand:
    card_list.remove(n)
print(card_list)

player2_hand = random.sample(range(len(card_list)), 7)
print(player2_hand)

for n in player2_hand:
    card_list.remove(n)

print(card_list)

# player2_hand = random.sample(range(len(card_list)), 7)




# print(player2_hand)
   

