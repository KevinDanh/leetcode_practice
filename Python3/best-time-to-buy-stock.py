class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        min = prices[0]
        for i in prices:
            if i < min:
                min = i
            if i - min > maxProfit:
                maxProfit = i - min
        return maxProfit