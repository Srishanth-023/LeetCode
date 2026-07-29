class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """

        # num_string = str(n)

        sum = 0
        pdt = 1

        # for num in num_string:
        #     temp = int(num)
        #     sum += temp
        #     pdt *= temp

        # return pdt - sum

        while not (n == 0):
            temp = n % 10
            sum += temp
            pdt *= temp
            n = n / 10

        return pdt - sum