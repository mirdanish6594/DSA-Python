arr = list(map(int, input("Enter the array: ").split()))
max_element = arr[0]

for num in arr:
    if num > max_element:
        max_element = num

print("largest element: ", max_element)