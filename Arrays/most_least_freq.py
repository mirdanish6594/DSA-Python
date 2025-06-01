arr = list(map(int, input("Enter array: ").split()))

freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
        
max_freq = max(freq.values())
min_freq = min(freq.values())

most_frequent = [key for key, val in freq.items() if val == max_freq]
least_frequent = [key for key, val in freq.items() if val == min_freq]

print("\nMost Frequent Elements(s): ", most_frequent, "->", max_freq, "times")
print("Least Frequent Element(s): ", least_frequent, "->", min_freq, "times")