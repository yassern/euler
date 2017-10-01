x = 2520
found = False

while not found:
    for i in range(20, 1, -1):
        if x % i != 0:
            break
        if i == 2:
            print(x)
            found = True
    x += 5;
