class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # clean_string = ""
        clean_string = []

        for character in s:
            if character.isalnum():
                # clean_string += character.lower()
                clean_string.append(character.lower())

        return clean_string == clean_string[::-1]