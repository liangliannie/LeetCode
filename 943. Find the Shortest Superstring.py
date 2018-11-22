class Solution2(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        
        def T_reduce(A):
            Max_length=0
            Start=""
            End=""
            K=len(A)
            for i in range(0,K):
                for j in range(0,K):
                    if i==j:
                        continue
                    for l in range(1,len(A[i])):
                        if len(A[i])-l<=Max_length:
                            break
                            
                        if( A[j].startswith(A[i][l:]) ):
                            Max_length=len(A[i])-l
                            End=A[j]
                            Start=A[i]
                    
                    for l in range(len(A[i])-1,0,-1):
                        if l<=Max_length:
                            break
                        if( A[j].endswith(A[i][:l]) ):
                            Max_length=l
                            End=A[i]
                            Start=A[j]
            #print Max_length,Start,End
            if(Max_length==0):
                Temp1=A.pop()
                Temp2=A.pop()
                A.append(Temp1+Temp2)
            else:
                A.remove(Start)
                A.remove(End)
                A.append(Start[:len(Start)-Max_length]+End)
                
            
        #print(A)
        while(len(A)>1):
            T_reduce(A)
            #print(A)
        return A[0]
    
    

class Solution3(object):
    
    def Overlapping(self, str1,str2):
        len1 = len(str1)
        len2 = len(str2)
        ans1,ans2,s1,s2=-1,-1,None,None
        for i in range(1,min(len1,len2)):
            if str1[:i]==str2[-i:]:
                ans1 = i
                s1 = str2+str1[i:]
            if str2[:i]==str1[-i:]:
                ans2 = i
                s2 = str1+str2[i:]
#         print([ans1, s1],[ans2, s2],[0,str1+str2])
        return max([[ans1, s1],[ans2, s2],[0,str1+str2]])
    
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        while len(A)>1:
            K = len(A)
            rans,ri,rj,rs=0,0,K-1,A[0]+A[K-1]
            for i in range(K):
                for j in range(K):
                    if i==j:
                        continue
                    ans,s = self.Overlapping(A[i], A[j])
                    if ans>rans:
                        rans,ri,rj,rs=ans,i,j,s
#                     print(rans,'rans',ri,rj)
            start,end = A[ri],A[rj]
            A.remove(start)
            A.remove(end)
            A.append(rs)
        return A[0]
    
class Solution(object):
    
    def shortestSuperstring(self, strings):
        N = len(strings)
        overlaps = [[0]*N for _ in xrange(N)]
        for i,x in enumerate(strings):
            for j,y in enumerate(strings):
                if i != j:
                    for k in xrange(min(len(x),len(y)),0,-1):
                        if x[:k]==y[-k:]:
                            overlaps[i][j] = k
                            break
        print(overlaps)
        dp = [[0] * N for _ in xrange(1<<N)]
        parent = [[None] * N for _ in xrange(1<<N)]
        for mask in xrange(1, 1<<N):# all possible combinations
            for j in xrange(N):# 
                if mask >> j & 1: #  check if j is inside the case
                    pmask = mask ^ 1<< j
                    if pmask == 0: continue
                    for i in xrange(N):
                        if (pmask >> i) & 1:
                            ans = dp[pmask][i] + overlaps[i][j]
                            if ans > dp[mask][j]:
                                dp[mask][j]= ans
                                parent[mask][j] = i
        allmask = (1<<N) - 1
        i  = max(xrange(N), key=lambda j: dp[-1][j])
        perm = []
#         print(overlaps)
        while i is not None:
            perm.append(i)
            mask, i = mask^(1<<i), parent[mask][i]
            
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in xrange(N) if not seen[i]])
        
        ans = [strings[perm[0]]]
#         print(["catg","ctaagt","gcta","ttca","atgcatc"])
        for i in xrange(1,len(perm)):
#             print(perm[i-1], perm[i])
            overlap = overlaps[perm[i]][perm[i-1]]
#             print(overlap)
            ans.append(strings[perm[i]][overlap:])
            
        return ''.join(ans)    
#         print(perm, )
            
        
                                
                    
                    
                    
                
            
                    
         
            
                        
                        

                    
    
    
        
#         
# f = Solution2()
# # f.Overlapping("ctaagt","gcta")
# # hello
# a = f.shortestSuperstring(["catg","ctaagt","gcta","ttca","atgcatc"])
# print(a)

f = Solution()
# f.Overlapping("catg","atgcatc")
# hello
a = f.shortestSuperstring(["catg","ctaagt","gcta","ttca","atgcatc"])
print(a)




    
    
    