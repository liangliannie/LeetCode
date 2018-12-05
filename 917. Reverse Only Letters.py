class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type S: str
        :rtype: str
        """
        l,r = 0,len(s)-1
        res = ['']*len(s)
        def isLetter(i):
            if (ord(i)>=ord('a') and ord(i)<=ord('z')) or ord(i)>=ord('A') and ord(i)<=ord('Z'):
                return True
            return False
        while l<=r:
            i = isLetter(s[l])
            j = isLetter(s[r])
            if i and j:
                res[l]=s[r]
                res[r]=s[l]
                l+=1
                r-=1
            elif i:
                res[r]=s[r]
                r-=1
            elif j:
                res[l]=s[l]
                l+=1
            else:
                res[l]=s[l]
                res[r]=s[r]
                l+=1
                r-=1
        return ''.join(res)