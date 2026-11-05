class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = buy + 1

        profit = 0

        while buy < sell and sell == len(prices):
            current_calc = buy - sell
            max = (profit, current_calc)
            sell += 1

            
        return profit