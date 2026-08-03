class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        richest = 0
        sum = 0

        for account in accounts:
            for wealth in account:
                sum = sum + wealth

            if sum > richest:
                richest = sum

            sum = 0

        return richest