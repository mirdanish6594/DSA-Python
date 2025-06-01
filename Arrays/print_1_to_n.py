def print_1_to_n(n, current=1):
    if current > n:
        return
    print(current)
    print_1_to_n(n, current + 1)

n = int(input("Enter the value of n: "))
print_1_to_n(n)
