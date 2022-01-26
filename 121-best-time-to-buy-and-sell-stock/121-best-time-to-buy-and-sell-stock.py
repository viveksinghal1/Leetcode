class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        boughtStk = prices[0]
        profit = 0
        
        lnt = len(prices)
        
        for i in range(1, lnt):
            if prices[i] < boughtStk:
                boughtStk = prices[i]
            elif (prices[i] - boughtStk) > profit:
                profit = prices[i] - boughtStk
        
        return profit