_sum = 2
fib = [1, 2]
next_value = 0

while next_value < 4000000:
    next_value = fib[len(fib) - 1] + fib[len(fib) - 2]
    if next_value % 2 == 0:
        _sum += next_value
    fib.append(next_value)

print(_sum)
