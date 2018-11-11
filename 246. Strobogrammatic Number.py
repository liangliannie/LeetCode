class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if '2' in num or '3' in num or '4' in num or '5' in num or '7' in num:
            return False
        
        if len(num)==0:
            return True
        if len(num)==1:
            if '6' in num or '9' in num:
                return False
            else:
                return True
        l = 0
        r = len(num)-1
        
        if (num[l]=='0' and num[r]=='0') or (num[l]=='1' and num[r]=='1') or (num[l]=='8' and num[r]=='8') or (num[l]=='6' and num[r]=='9') or (num[l]=='9' and num[r]=='6'):
            return self.isStrobogrammatic(num[1:-1])
        else:
            return False