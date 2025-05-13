def left_rotate_by_one(arr):
    first = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]

    arr[-1] = first

arr = list(map(int, input("Enter the array: ").split()))
left_rotate_by_one(arr)
print("The new array is: ", arr)