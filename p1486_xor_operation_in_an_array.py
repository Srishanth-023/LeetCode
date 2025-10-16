class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """

        nums = []

        for i in range(n):
            temp = start + 2 * i
            nums.append(temp)

        xor = 0
        for num in nums:
            xor ^= num

        return xor


        # # O(1) --> Space complexity 
        # xor = 0
        # for i in range(n):
        #     xor ^= start + 2 * i

        # return xor