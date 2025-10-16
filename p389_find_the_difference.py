class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        hash_map = {}

        for letter in t:
            if letter in hash_map:
                hash_map[letter] += 1
            else:
                hash_map[letter] = 1
        
        for letter in s:
            if letter in hash_map:
                hash_map[letter] -= 1
                if hash_map[letter] == 0:
                    del hash_map[letter]

        for key in hash_map:
            return key