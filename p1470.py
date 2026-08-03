class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        shuffled_array = []

        for index, num in enumerate(nums):
            if index % 2 == 0:
                shuffled_array.append(nums[index / 2])
            else:
                shuffled_array.append(nums[n + (index / 2)])

        return shuffled_array