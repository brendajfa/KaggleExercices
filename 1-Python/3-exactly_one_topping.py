def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    pass
    return (not ketchup and not mustard and onion) or (ketchup and not mustard and not onion) or (not ketchup and mustard and not onion)


""" 
Solution: This condition would be pretty complicated to express using just and, or and not, but using boolean-to-integer conversion gives us this short solution:

return (int(ketchup) + int(mustard) + int(onion)) == 1
Fun fact: we don't technically need to call int on the arguments. Just by doing addition with booleans, Python implicitly does the integer conversion. So we could also write...

return (ketchup + mustard + onion) == 1
"""
