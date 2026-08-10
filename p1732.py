class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        altitude = []
        altitude.append(0)
        temp = altitude[0]
        greatest = altitude[0]

        for index, alt in enumerate(gain):
            temp += alt
            altitude.append(temp)

            if altitude[index + 1] > greatest:
                greatest = altitude[index + 1]

        return greatest