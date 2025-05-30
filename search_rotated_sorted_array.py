from typing import List

class Solution:
    def targetRotated(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid -1 
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid = 1
    
        return -1
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    target = int(input("Enter the target: "))

    sol = Solution()
    result = sol.targetRotated(nums, target)
    print("Target index is: ", result)