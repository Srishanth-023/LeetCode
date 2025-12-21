class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        words = s.split() # Can add strip() ??

        length_of_last_word = len(words[-1])

        return length_of_last_word

        # if not words:
        #     return 0
        # else:
        #     return length_of_last_word