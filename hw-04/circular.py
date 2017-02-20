#!/usr/bin/env python

# at the end your answer
# should be in solution
solution = 0

# First calculate the
# Sieve of Eratosthenes
# up to a million.
N = 1000000

# initialize an array of flags
is_prime = [False, False]+[True for x in range(2,N+1)]

p = 2
for p in range(2,N+1):
    if is_prime[p] == True:
        idx = p + p
        while idx < N:
            is_prime[idx] = False
            idx += p
    p += 1

# iterate over all integers up to N and update the is_prime array accordingly
primes = []
for x in range(N):
    if is_prime[x] == True:
        primes.append(x)

# Now loop over those primes,
# And ask in each case if it's
# a circular prime
def rotations(number):
    lst = str(number)
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    rotate = []
    for i in range(len(lst)):
        start = lst[i:]
        end = lst[:i]
        final = start + end
        rotate.append(final)
    return rotate

is_circular = [False for i in is_prime]
for i in primes:
    is_circular[i] = True

for i in primes:
    perms = rotations(i)
    for j in perms:
        if int(j) not in primes:
            is_circular[i] = False
            break

circular = []

for x in range(N):
    if is_circular[x] == True:
        circular.append(x)

solution = len(circular)
