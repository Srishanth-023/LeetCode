class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        running_sum_array = []
        sum = 0

        for num in nums:
            sum += num
            running_sum_array.append(sum)

        # for i in range(1, len(nums)):  # No need for new Array
        #     nums[i] += nums[i-1]

        # return nums

        return running_sum_array