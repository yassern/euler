def is_palindrome(string):
    if len(string) < 2:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False

largest_palindrome = 0
for i in range(999, 99, -1):
    for j in range(999, i - 1, -1):
        mult = i * j
        if is_palindrome(str(mult)):
            largest_palindrome = max(largest_palindrome, mult)
print(largest_palindrome)
