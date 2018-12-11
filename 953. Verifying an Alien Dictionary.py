class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        nwords = sorted(words, key=lambda word: [order.index(i) for i in word])
        if nwords == words:
            return True
        return False
        