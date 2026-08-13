class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # answer = []

        # for i in range(0, len(nums)):
        #     answer.append(nums[nums[i]])

        # return answer

        return [nums[nums[i]] for i in range(0, len(nums))]