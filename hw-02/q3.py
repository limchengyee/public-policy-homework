#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0
number   = 175832868806

# First create a list of prime numbers to 300.
prime = [2]
i=1

while i <= 300:
    i += 1
    for n in prime:
        is_prime = True
        if i % n == 0:
            is_prime = False
            break

    if is_prime == True:
        prime.append(i)

# Now which of these are factors of 175832868806
factor = []
for n in prime:
    if number % n == 0:
        factor.append(n)
        solution += 1

# Check for the correct answer.
print("#3 : Count Prime Factors ::", solution, "Correct." if solution == 6 else ("Wrong: " + str(solution)))
