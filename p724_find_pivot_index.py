class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, sum(nums)

        for index, value in enumerate(nums):
            right = right - value
            if right == left:
                return index

            # if left * 2 + value == right:
            #   return index
            
            left = left + value

        return -1
        