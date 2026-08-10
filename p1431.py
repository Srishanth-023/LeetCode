class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        greatest = 0

        for candy in candies:
            if candy > greatest:
                greatest = candy

        for index, candy in enumerate(candies):
            candy += extraCandies

            if candy >= greatest:
                candies[index] = True
            else:
                candies[index] = False
        
        return candies