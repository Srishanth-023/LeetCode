class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = []

        for char in s:
            if char not in seen:
                seen.append(char)
            else:
                return char
                exit
        