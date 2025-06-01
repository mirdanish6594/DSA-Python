# Optimal Reversal Algorithm
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate_by_d(arr, d):
    n = len(arr)
    d %= n
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)

arr = list(map(int, input("Enter the array: ").split()))
d = int(input("Enter the no. of positions you want the array to rotate left by: "))
left_rotate_by_d(arr, d)
print("Array after rotating: ", arr)