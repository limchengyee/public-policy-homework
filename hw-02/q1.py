#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0

# Your code goes here.
# Should be about 10 lines.
factors = [4, 13, 14, 26, 50]
b = 0

while b < 9:
    solution += 1
    is_multiple = True

    for n in factors:
        if not solution % n == 0:
            is_multiple = False

    if is_multiple == True:
        b += 1
# Check for the correct answer.
print("#1 : 9th multiple ::", solution, "Correct." if solution == 81900 else ("Wrong: " + str(solution)))
