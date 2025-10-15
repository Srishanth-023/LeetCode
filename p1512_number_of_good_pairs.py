class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        frequency = {}
        count = 0

        for num in nums:
            if num in frequency:
                count += frequency[num]
                frequency[num] += 1
            else:
                frequency[num] = 1

        return count