class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # count_array = []
        # count = 0

        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         if nums[i] > nums[j]:
        #             count += 1
            
        #     count_array.append(count)
        #     count = 0

        # return count_array

        return [sorted(nums).index(i) for i in nums]