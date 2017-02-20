#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0

# Your code goes here.
# Should be < 10 lines.
from math import factorial
solution = factorial(200)/(factorial(100)*factorial(100))
print("#6 : Grid ::", solution)
