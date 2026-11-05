class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1):
            for j in range(i, len(prices)):
                current_calc = prices[j] - prices[i]
                profit = max(current_calc, profit)
        
        return profit