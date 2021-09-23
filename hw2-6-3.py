# Author: ATN 9/21/21

# Assigning values

free_throws = input("How many free throws? ")
basket = input("How many two point baskets? ")
basket_three_point = input("How many three point baskets? ")

# Final calculations

points = (int(free_throws)) + (int(basket) * 2) + (int(basket_three_point) * 3)

print("The player scored " + str(points) + " points in the game.")
