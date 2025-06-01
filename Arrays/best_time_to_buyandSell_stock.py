from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
    
if __name__ == "__main__":
    prices = list(map(int, input("Enter the values of stocks: ").split()))

    solution = Solution()
    result = solution.maxProfit(prices)
    print("Maximum profit: ", result)