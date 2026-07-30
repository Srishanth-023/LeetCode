class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        res1 = (nums[0] + nums[1]) > nums[2]
        res2 = (nums[0] + nums[2]) > nums[1]
        res3 = (nums[1] + nums[2]) > nums[0]

        if res1 and res2 and res3:
            if nums[0] == nums[1] and nums[0] == nums[2]:
                return "equilateral"
            elif nums[0] != nums[1] and nums[0] != nums[2] and nums[1] != nums[2]:
                return "scalene"
        else:
            return "none"

        return "isosceles"