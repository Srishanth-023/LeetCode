class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # str1 = str(num)
        # rev_str1 = str1[::-1]
        # num1 = int(rev_str1)

        # str2 = str(num1)
        # rev_str2 = str2[::-1]
        # num2 = int(rev_str2)

        # if num2 == num:
        #     return True
        # else:
        #     return False

        if num == 0:
            return True
        elif num % 10 == 0:
            return False
        
        return True
