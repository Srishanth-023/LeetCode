class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number_of_digits = []
        even_number_digits = 0

        for num in nums:
            num = abs(num)
            count = 0
            
            if num == 0:
                count = 1
            else:
                while num > 0:
                    num //= 10
                    count += 1

            number_of_digits.append(count)

        for num in number_of_digits:
            if num % 2 == 0:
                even_number_digits += 1
            else:
                pass

        return even_number_digits

        