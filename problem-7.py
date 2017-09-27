primes = [2]
next_number = primes[-1] + 1

while len(primes) < 10001:
    for prime in primes:
        if next_number % prime == 0:
            break
        if prime == primes[-1]:
            primes.append(next_number)
    next_number += 1

print(primes[-1])
