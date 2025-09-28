class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        numbers = []
        for i in range(1, (n // 2) + 1):
            numbers.append(i)
            numbers.append(-i)
        
        if n % 2 == 1:
            numbers.append(0)

        return numbers