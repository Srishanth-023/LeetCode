class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        for i in range(0, int(len(s) / 2)):
            temp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = temp

        return s

        # length = len(s)
        # end = int(length / 2)
        
        # for i in range(0, end):
        #     temp = s[i]
        #     s[i] = s[length - 1 - i]
        #     s[length - 1 - i] = temp

        # return s