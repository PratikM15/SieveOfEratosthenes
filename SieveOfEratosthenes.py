def SieveOfEratosthenes(n):
    primes = []
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return primes

def main():
    T = int(input())
    for _ in range(T):
        L, R = input().split()
        L = int(L)
        R = int(R)
        primes = SieveOfEratosthenes(R)
        primes = [prime for prime in primes if prime >= L]
        if primes != []:
            print(max(primes)-min(primes))
        else:
            print(-1)

main()
