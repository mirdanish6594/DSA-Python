from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        
        return answer

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    sol = Solution()
    result = sol.productExceptSelf(nums)
    print("Output: ", result)
