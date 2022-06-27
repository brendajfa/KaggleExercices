def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    
    resta = player_total - player_low_aces - player_high_aces * 11
    hit = False
    dif = player_total - dealer_total
    #print(player_high_aces)
    if player_total <= 17 and  dealer_total >= 10:
        return True   
    else:
        for i in range(player_high_aces):
            new_hand = resta + (player_low_aces + i) + (player_high_aces - i) * 11 
       
            if ((21-new_hand) <= 2) :
                False
            elif (new_hand < 21 and player_high_aces != 0) or (new_hand < 21 and dealer_total < player_total):
                hit = True
            else:
                hit = False
        return(hit)




""" Player won 20117 out of 50000 games (win rate = 40.2%)
"""
