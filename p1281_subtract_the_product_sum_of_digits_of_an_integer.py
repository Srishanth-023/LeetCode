class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """

        productOfDigits, sumOfDigits = 1, 0
        n = str(n)

        for num in n:
            productOfDigits *= int(num)
            sumOfDigits += int(num)

        return productOfDigits - sumOfDigits