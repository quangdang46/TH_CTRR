def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def printPrime(N):
    primes = []
    for i in range(2, N):
        if is_prime(i):
            primes.append(i)
    return primes

print(printPrime(100))