# Author: ATN 9/21/21

import math

radius = input("Enter radius of the cylinder: ")
height = input("Enter height of the cylinder: ")

# Calculations

volume = math.pi * float(radius) ** 2 * float(height)
surface_area = 2 * math.pi * float(radius) * (float(height) + float(radius))

print("Volume is " + str(float(volume)))
print("Surface area is " + str(float(surface_area)))
