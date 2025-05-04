def print_something(n, count=1):
    if count > n:
        return
    print("Hello")
    print_something(n, count + 1)

n = int(input("How many times you want to print? "))
print_something(n)

