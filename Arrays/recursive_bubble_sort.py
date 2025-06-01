def recursive_bubble_sort(arr, n):
    if n == 1:
        return 
    for i in range (n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    recursive_bubble_sort(arr, n-1)

arr = list(map(int, input("Enter the array: ").split()))
recursive_bubble_sort(arr, len(arr))
print("Sorted array: ", arr)