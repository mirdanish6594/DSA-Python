from collections import deque
from typing import List

class Solution:
    def SlidingMax(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            if dq[0] <= i - k:
                dq.popleft()

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    k = int(input("Enter the value of interval: "))

    sol = Solution()
    result = sol.SlidingMax(nums, k)
    print("The new array is: ", result)

