alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
total_candies = alice_candies + bob_candies + carol_candies
to_smash = total_candies - ( total_candies // 3 ) * 3


# Another anwser would be: to_smash = (alice_candies + bob_candies + carol_candies) % 3
