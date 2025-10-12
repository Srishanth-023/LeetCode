class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        # # Submission not accepted --> Memory limit exceeded !!
        # interval_list = []
        # odd_list= []

        # for num in range(low, high + 1):
        #     interval_list.append(num)

        # for num in interval_list:
        #     if num % 2 == 1:
        #         odd_list.append(num)

        # return len(odd_list)

        
        # Mathematical approach
        return ((high + 1) // 2) - (low // 2)  # (n + 1) / 2 (count of odd with n numbers)