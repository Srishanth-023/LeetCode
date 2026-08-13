class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # answer = []

        # for i in range(0, 2 * (len(nums))):
        #     if i < len(nums):
        #         answer.append(nums[i])
        #     else:
        #         answer.append(nums[i - len(nums)])
            

        # return answer

        return [nums[i] if i < len(nums) else nums[i - len(nums)] for i in range(0, 2 * (len(nums)))]