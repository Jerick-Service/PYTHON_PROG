from helpers.string import shout
from helpers.math import area

# Calculate the area
length = 5
width = 8
result = area(length, width)

# Print the result using shout
print(shout(f"The area of a {length}-by-{width} rectangle is {result}"))