#--------------
# Set - 6.5
#--------------
from check_type_decorator import check_type

#=====================================
# "Set" game:
# 81 different cards with 4 properties:
# 1. color: red, green, purple
# 2. shape: diamond, squiggle, oval
# 3. number of shapes: 1, 2, 3
# 4. fill: empty, full, striped
#=====================================

import random

color = {"red", "green", "purple"}
shape = {"diamond", "squiggle", "oval"}
number = {"1", "2", "3"}
fill = {"empty", "full", "striped"}

#=======================================================================================
### 1st section ####
#-------------------
# list of all the cards:
cards = [ [c, s, n, f] for c in color for s in shape for n in number for f in fill]
#=======================================================================================


#=======================================================================================
### 2nd section ####
#-------------------
# get 12 random cards function:
#-------------------------------
def get_12_random_cards():
    return list(random.sample(cards, 12))
#=======================================================================================


#=======================================================================================
### 3rd section ####
#-------------------------------------------
# is_set function: 
# get 3 cards.
# return True if the 3 cards are a set.
#-------------------------------------------
def is_set(card1, card2, card3):
    return 2 not in [len({card1[i], card2[i], card3[i]}) for i in range(4)]

#-------------------------------------------
# get_all_sets function:
# get a list of cards.
# return a list of all the sets in the list of cards.
#-------------------------------------------
@check_type(list)
def get_all_sets(cards):
    return [(cards[i], cards[j], cards[k]) for i in range(len(cards))
             for j in range(i+1, len(cards))
               for k in range(j+1, len(cards)) 
               if is_set(cards[i], cards[j], cards[k])]
                    

@check_type(int)             
def get_percentage_of_successes(num_ofsamples):
    num_of_success = 0
    for i in range(num_ofsamples):
        cards = get_12_random_cards()
        if get_all_sets(cards): # if there is at least one set in the 12 cards
            num_of_success += 1
    return (num_of_success / num_ofsamples * 100).__round__(2)

#=======================================================================================

def main():
    cards = get_12_random_cards()
    print(f"cards: \n {cards} \n")

    print(f"number of sets:  {len(get_all_sets(cards))}")
    print(f"sets:  \n {get_all_sets(cards)} \n")

    print(f"percentage of success (10000 samples) = {get_percentage_of_successes(10000)}%")

if __name__ == "__main__":
    main()
