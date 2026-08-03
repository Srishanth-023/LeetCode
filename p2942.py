class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """

        indices_array = []

        for index, word in enumerate(words):
            if x in word:
                indices_array.append(index)


        return indices_array