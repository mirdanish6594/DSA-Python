def reverse_array(arr, first, last):
    if first >= last:
        return 
    arr[first], arr[last] = arr[last], arr[first]
    reverse_array(arr, first + 1, last - 1)

arr = list(map(int, input("Enter array: ").split()))
reverse_array(arr, 0, len(arr) - 1)
print("Reversed array: ", arr)