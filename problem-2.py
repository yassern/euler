_sum = 2
fib = [1, 2]

while True:
    next_value = fib[len(fib) - 1] + fib[len(fib) - 2]
    if next_value > 4000000:
        break
    if next_value % 2 == 0:
        _sum += next_value
    fib.append(next_value)

print(_sum)
