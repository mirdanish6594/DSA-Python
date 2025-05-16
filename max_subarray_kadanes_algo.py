from typing import List 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
    
if __name__ == "__main__":
    nums= list(map(int, input("Enter the array: ").split()))

    solution = Solution()
    result = solution.maxSubArray(nums)

    print("Max subarray sum: ", result)