def recursive_insertion_sort(arr, n):
    if n<= 1:
        return 
    recursive_insertion_sort(arr, n-1)
    key = arr[n-1]
    j = n-2
    while j>=0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

arr = list(map(int, input("Enter the array: ").split()))
recursive_insertion_sort(arr, len(arr))
print("Sorted array: ", arr)