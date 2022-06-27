def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies == 1 :
        cand = "candy"
    else:
        cand = "candies"
    print("Splitting", total_candies, cand)
    return total_candies % 3

to_smash(91)
to_smash(1)
