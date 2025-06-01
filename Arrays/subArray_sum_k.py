from typing import List 
from collections import defaultdict

class Solution:
    def subArray(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_map = defaultdict(int)

        prefix_map[0] = 1

        for num in nums:
            current_sum += num
            count += prefix_map[current_sum - k]
            prefix_map[current_sum] += 1

        return count
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    k = int(input("Enter the value of k: "))

    sol = Solution()
    result = sol.subArray(nums, k)
    print("Max subarray: ", result)