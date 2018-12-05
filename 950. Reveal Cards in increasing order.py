class Solution(object):
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        res = [deck.pop()]
        while deck:
            res = [deck.pop(), res.pop()] + res
        return res