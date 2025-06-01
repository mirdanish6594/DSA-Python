arr = list(map(int, input("Enter array: ").split()))

freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
        
print("Frequencies of elements: ")
for key in freq:
    print(f"{key} -> {freq[key]} times")