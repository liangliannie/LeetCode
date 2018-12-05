import collections 

class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        q = collections.deque(tokens)
        max_points,cur = 0,0
        while len(q)>=1 and P>=q[0] or cur:
            if not q:
                break
#             print(q,cur,P)
            if P>=q[0]:
                P-=q.popleft()
                cur +=1
            elif cur > 0:
                P+=q.pop()
                cur -=1
            max_points = max(max_points, cur)
        
#         print(q,P)
            
        
        return max_points
    
class Solution2(object):
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        deque = collections.deque(tokens)
        ans = bns = 0
        while deque and (P >= deque[0] or bns):
            while deque and P >= deque[0]:
                P -= deque.popleft()
                bns += 1
            ans = max(ans, bns)

            if deque and bns:
                P += deque.pop()
                bns -= 1

        return ans   

s=Solution()
tokens =[100]
P = 50
print(s.bagOfTokensScore(tokens, P))


print(s.bagOfTokensScore([100,200,300,400], 200))