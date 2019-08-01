import math

def primes(n):
    """ Return a list of the prime numbers <= n."""
    sieve = [True]*(n//2)
    for i in range(3, int(math.sqrt(n))+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n - i*i - 1) // (2*i) +1)
    return [2] + [2*i+1 for i in range(1, n // 2) if sieve[i]]

n = 1000000

P = set(primes(n))

# A list of integers 2^i-1 <= n

A = []

for i in range(2, int(math.log(n+1, 2))+1):
    A.append(2**i - 1)

# The set of Mersenne primes as the intersection of P and A

M = P.intersection(A)

# Output as a sorted list of M
print(sorted(list(M)))
