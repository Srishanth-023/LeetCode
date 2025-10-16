class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # # O(n) --> Space & Time complexity
        # result = []

        # for num in nums:
        #     result.append(nums[num])

        # return result


        # # 0(1) --> Space complexity || O(n) --> Time complexity
        length = len(nums)
        const = length + 1

        for num in range(length):
            a = nums[num]
            b = nums[a] % const
            nums[num] = a + const * b

        for num in range(length):
            nums[num] /= const

        return nums