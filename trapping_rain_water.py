from typing import List

class Solution:
    def maxWater(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[n-1] =height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        total_water = 0
        for i in range(n):
            total_water += min(left_max[i], right_max[i]) - height[i]

        return total_water
    
if __name__ == "__main__":
    heights = list(map(int, input("Enter the array: ").split()))
    sol = Solution()
    result = sol.maxWater(heights)
    print("Total trapped water: ", result)