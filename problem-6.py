from functools import reduce

interval = list(range(1, 101))

sum_of_the_squares = reduce(lambda _sum, x: _sum + (x ** 2), interval)
square_of_the_sum = (sum(interval))**2

print(square_of_the_sum - sum_of_the_squares)
