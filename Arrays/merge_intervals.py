from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array as space seperated pairs: ").strip().split()))

    intervals = [nums[i:i+2] for i in range(0, len(nums), 2)]

    solution = Solution()
    result = solution.merge(intervals)

    print("Merged Intervals:", result)
