from typing import List

class Solution:
    def longestSequence(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num -1 not in num_set:
                current_sum = num
                current_streak = 1

                while current_sum + 1 in num_set:
                    current_sum += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))

    sol = Solution()
    result = sol.longestSequence(nums)
    print("Longest sequence: ", result)