def primes_until(max):
    primes = []
    numbers = list(range(2, max))

    for i in range(0, len(numbers)):
        if(numbers[i] != 0):
            primes.append(numbers[i])
            index_discard = i + numbers[i]
            while (index_discard < len(numbers)):
                numbers[index_discard] = 0
                index_discard += numbers[i]
    return primes

print(sum(primes_until(2000000)))
