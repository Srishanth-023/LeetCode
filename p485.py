class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count, highest_count = 0, 0

        for num in nums:
            if num == 1:
                count += 1
                # if count > highest_count:
                #     highest_count = count
            else:
                highest_count = max(highest_count, count);
                count = 0

        # return highestCount;
        return highest_count if highest_count > count else count