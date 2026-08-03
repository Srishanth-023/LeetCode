class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum = 0
        count = 0

        for num in nums:
            sum += num

            if sum == 0:
                count += 1;

        return count    