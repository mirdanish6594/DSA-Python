from typing import List

class Solution:
    def reverseArray(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def reverse(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    k = int(input("Enter the value of k: "))

    sol = Solution()
    sol.reverseArray(nums, k)
    print("The reversed array is: ", nums)