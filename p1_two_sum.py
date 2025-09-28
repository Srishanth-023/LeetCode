class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        previousHashMap = {}

        for currentIndex, num in enumerate(nums):
            difference = target - num
            if difference in previousHashMap:
                return [previousHashMap[difference], currentIndex]
            
            previousHashMap[num] = currentIndex

        return 

        