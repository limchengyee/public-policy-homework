#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0

# Your code goes here.
# Should be about 10 lines.
a, b = 1, 1
fibo = []
max_fibo = 1000000000

while a < max_fibo:
    fibo.append(a)
    c = a + b
    a = b
    b = c

for i in fibo:
    if i % 17 == 0:
        solution += i

# Check for the correct answer.
print("#2 : Fibonacci ::", solution, "Correct." if solution == 15129388 else ("Wrong: " + str(solution)))
