class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        count = 0
        numberStr = str(num)

        for ch in numberStr:
            tempInt = int(ch)

            if (num % tempInt == 0):
                count += 1

        return count
        