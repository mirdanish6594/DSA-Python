from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> List[int]:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    sol = Solution()
    result = sol.findDuplicate(nums)
    print("The duplicate is: ", result)