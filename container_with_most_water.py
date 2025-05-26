from typing import List

class Solution:
    def mostWater(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
if __name__ == "__main__":
    heights = list(map(int, input("Enter the array of heights: ").split()))
    sol = Solution()
    result = sol.mostWater(heights)
    print("The max area is: ", result)