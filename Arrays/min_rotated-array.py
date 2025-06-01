from typing import List

class Solution:
    def minArray(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid

        return nums[left]
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array in spaced way: ").split()))
    sol = Solution()

    min = sol.minArray(nums)
    print("Min element: ", min)