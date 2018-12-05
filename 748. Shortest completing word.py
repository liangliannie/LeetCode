class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        def CheckIfValid(w, dic):
            d = {}
            for s in w:
                if s not in d:
                    d[s]=1
                else:
                    d[s]+=1
                    
            for it in dic:
                if it not in d:
                    return False
                else:
                    if dic[it]>d[it]:
                        return False
            return True
            
        dic = {}
        for i in licensePlate:
            if ord(i.lower())>=ord('a') and ord(i.lower())<=ord('z'): 
                s = i.lower()
                if s not in dic:
                    dic[s]=1
                else:
                    dic[s]+=1
        words.sort(key=lambda word: len(word))
        for w in words:
            if CheckIfValid(w, dic):
                return w