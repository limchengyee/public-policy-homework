#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0

# create a function that returns
# the next value in the collatz sequence.
# If you call it recursively, keep track of the depth.

def colltaz(n,m=1):
    if n == 1:
        return m
    else:
        if n % 2 == 0:
            m += 1
            return colltaz(n/2, m)

        else:
            m += 1
            return colltaz(3*n + 1, m)

# now loop up to 2 million,
# using that function
length = []
a = 0
while a < 2000000:
    a += 1
    b = colltaz(a)
    length.append(b)

solution = max(length)
print("#7 : Collatz Sequence ::", solution)
