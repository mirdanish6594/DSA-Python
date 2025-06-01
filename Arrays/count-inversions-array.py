from typing import List

class Solution:
    def countInversions(self, nums: List[int]) -> int:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            
            mid = len(arr) // 2
            left, left_inv  = merge_sort(arr[:mid])
            right, right_inv = merge_sort(arr[mid:])

            merged, cross_inv = merge(left, right)
            return merged, left_inv + right_inv + cross_inv
        
        def merge(left, right):
            i = j = 0
            merged = []
            inversions = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1

                else:
                    merged.append(right[j])
                    inversions += len(left) - i
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, inversions
        
        _, total_inversions = merge_sort(nums)
        return total_inversions
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array: ").split()))
    sol = Solution()

    result = sol.countInversions(nums)
    print("No. of inversions: ", result)
