def primes(number: int) -> int:
    pass


def primes2(number: int) -> int:
    pass


def primes3(number: int) -> int:
    pass


def primes4(number: int) -> int:
    pass


def eratosthenes(number: int) -> int:
    sieve = list(range(number + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    count = len([x for x in sieve if x != 0])
    return count
