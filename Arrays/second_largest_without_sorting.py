arr = list(map(int, input("Enter the array: ").split()))
if len(arr) < 2:
    print("The array should have atleast 2 elements.")

else:
    first = second = float('-inf') #set to -infinity so every element will be larger than this

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    
    if second == float('-inf'):
        print("No second largest element")
    else: 
        print("Second largest element is ", second)