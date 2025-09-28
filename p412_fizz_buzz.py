class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        fizz_buzz_array = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                fizz_buzz_array.append("FizzBuzz")
            elif i % 3 == 0:
                fizz_buzz_array.append("Fizz")
            elif i % 5 == 0:
                fizz_buzz_array.append("Buzz")
            else:
                fizz_buzz_array.append(str(i))
        
        return fizz_buzz_array