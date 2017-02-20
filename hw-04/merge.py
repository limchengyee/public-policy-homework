i = 7293
j = [int(v) for v in str(i)]
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

is_circular = [True for i in primes]
c = 0
for i in primes:
    c += 1

print(c)


for i in primes:
    number = [int(v) for v in str(i)]
    if len(number) > 1 and (2 in number or 4 in number or 6 in number or 8 in number or 0 in number):
        print(i)
        primes.remove(i)
