class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                currentProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, currentProfit)
            else:
                l = r
            
            r += 1

        return maxProfit
        