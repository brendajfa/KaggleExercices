import math
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    length = len(arrivals)
    position = arrivals.index(name)+1
    if(position > math.ceil(length/2)  and position < length):
        return True
    else:
        return False
    pass




"""
Solution:

def fashionably_late(arrivals, name):
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1

"""
