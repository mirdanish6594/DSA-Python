def remove_duplicates(arr):
    if not arr:
        return 0
    
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i +=  1
            arr[i] = arr[j]
    
    return i + 1

arr = list(map(int, input("Enter the array: ").split()))
k = remove_duplicates(arr)
print("Array without duplicates is: ", arr[:k])