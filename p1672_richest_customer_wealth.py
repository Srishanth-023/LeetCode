class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        total_wealth = 0
        total_wealth_for_each_customer = []
        
        for account in accounts:
            total_wealth = 0
            for wealth in account:
                total_wealth += wealth
                total_wealth_for_each_customer.append(total_wealth)

        maximum_wealth = total_wealth_for_each_customer[0]

        for wealth_for_each_customer in total_wealth_for_each_customer:
            if wealth_for_each_customer > maximum_wealth:
                maximum_wealth = wealth_for_each_customer

        return maximum_wealth