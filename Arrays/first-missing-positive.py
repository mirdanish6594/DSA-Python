from typing import List

class Solution:
    def missingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] < n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

            for i in range(n):
                if nums[i] != i + 1:
                    return i + 1
                
            return n + 1
        
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    sol = Solution()

    result = sol.missingPositive(nums)
    print("The missing positive is: ", result)
                                                                     