#from learntools.core import binder; binder.bind(globals())
#from learntools.python.ex7 import *
#print('Setup complete.')

def hand_total(hand):
    sum_hand = sum([int(hand[index]) for index in range(len(hand)) if hand[index].isdigit()]) + (hand.count('J') + hand.count('Q') +hand.count('K') )*10
    a_hand = hand.count('A')
    final_hand = sum_hand
    for pre_index in range(hand+1):
        addition = pre_index*10+a_hand
        if addition +sum_hand < 21 or pre_index == 0:
            final_hand = addition+sum_hand
        else:
            break
    
    return final_hand


def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
   # >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    #>>> blackjack_hand_greater_than(['K'], ['10'])
    False
    #>>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """

    print("Cards of hand_1: {}\nCards of hand_2: {}".format(hand_1, hand_2))

    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)


print("Wrong") if blackjack_hand_greater_than(['K'], ['3', '4']) == "False" else print("Right")
print("Wrong") if blackjack_hand_greater_than(['A','10','10','A'], ['10']) == "True" else print("Right")
print("Wrong") if blackjack_hand_greater_than(['A', 'A', '2'], ['3']) == "True" else print("Right")
# Check your answer
#q3.check()


# SOLUTION
# def hand_total(hand):
#     """Helper function to calculate the total points of a blackjack hand.
#     """
#     total = 0
#     # Count the number of aces and deal with how to apply them at the end.
#     aces = 0
#     for card in hand:
#         if card in ['J', 'Q', 'K']:
#             total += 10
#         elif card == 'A':
#             aces += 1
#         else:
#             # Convert number cards (e.g. '7') to ints
#             total += int(card)
#     # At this point, total is the sum of this hand's cards *not counting aces*.

#     # Add aces, counting them as 1 for now. This is the smallest total we can make from this hand
#     total += aces
#     # "Upgrade" aces from 1 to 11 as long as it helps us get closer to 21
#     # without busting
#     while total + 10 <= 21 and aces > 0:
#         # Upgrade an ace from 1 to 11
#         total += 10
#         aces -= 1
#     return total

# def blackjack_hand_greater_than(hand_1, hand_2):
#     total_1 = hand_total(hand_1)
#     total_2 = hand_total(hand_2)
#     return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)