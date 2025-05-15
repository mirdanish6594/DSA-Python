from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - nums[i]

            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[num] = i

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    target = int(input("Enter the target: "))

    solution = Solution()
    result = solution.twoSum(nums, target)
    print("indices of elements that sum to target: ", result)
