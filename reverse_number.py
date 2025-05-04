def reverse_num(n):
    rev = 0
    while n > 0:
        rev = rev*10 + n%10
        n //= 10
    return rev

print(reverse_num(12345))