#from learntools.core import binder; binder.bind(globals())
#from learntools.python.ex7 import *
#print('Setup complete.')


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

    max_range = max(len(hand_1),len(hand_1))
    sum_hand_1 = sum([int(hand_1[index]) for index in range(len(hand_1)) if hand_1[index].isdigit()]) + (hand_1.count('J') + hand_1.count('Q') +hand_1.count('K') )*10
    sum_hand_2 = sum([int(hand_2[index]) for index in range(len(hand_2)) if hand_2[index].isdigit()]) + (hand_2.count('J') + hand_2.count('Q') +hand_2.count('K') )*10
    a_hand_1 = hand_1.count('A')
    a_hand_2 = hand_2.count('A')
    
#    print("Number of 'A' in hand_1: {}\nNumber of 'A' in hand_2: {}".format(a_hand_1, a_hand_2))

    final_hand_1 = sum_hand_1
    for pre_index_1 in range(a_hand_1+1):
        addition = pre_index_1*10+a_hand_1
#        print("pre_index_1: {} and addition: {}".format(pre_index_1,addition))
        if addition+sum_hand_1 < 21 or pre_index_1 == 0:
            final_hand_1 = addition+sum_hand_1
        else:
            break

    final_hand_2 = sum_hand_2
    for pre_index_2 in range(a_hand_2+1):
        addition = pre_index_2*10+a_hand_2
        if addition+sum_hand_1 < 21 or pre_index_2 == 0:
            final_hand_2 = addition+sum_hand_2
        else:
            break

    print("Sum of cards of hand_1: {}\nSum of cards of hand_2: {}".format(final_hand_1, final_hand_2))
    result = False
    if final_hand_1 <= 21:
        if final_hand_1 > final_hand_2 or final_hand_2 > 21:
            result = True
    return result


print("Wrong") if blackjack_hand_greater_than(['K'], ['3', '4']) == "False" else print("Right")
print("Wrong") if blackjack_hand_greater_than(['A','10','10','A'], ['10']) == "True" else print("Right")
print("Wrong") if blackjack_hand_greater_than(['A', 'A', '2'], ['3']) == "True" else print("Right")
# Check your answer
#q3.check()
