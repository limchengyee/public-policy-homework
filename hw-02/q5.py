#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0

# You _could_ use here the square root function, sqrt.
# It returns a floating point value
# sqrt(9) -> 3.0 but sqrt(10) -> 3.162...
# Note that you don't _need_ the square root.
from math import sqrt

# Your code goes here.
# Should be < 10 lines.
def squared(v):
    return v * v

for a in range(1,1000):
    for b in range(a,1000):
        c = sqrt(squared(a) + squared(b))
        if a + b + c == 1000:
            solution = a * b * c
# Check for the correct answer.
print("#5 : Pythagorean Triplet ::", solution, "Correct." if solution == 31875000 else ("Wrong: " + str(solution)))
