class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def commonfactor(x1,y1):
            x,y = abs(x1),abs(y1)
            if x==y:
                if x==1:
                    return False
                else:
                    return True
            if x>y:
                for i in xrange(2,x/2+1):
                    if x%i == 0 and y%i==0:
                        return True
                return False
            else:
                for i in xrange(2,y/2+1):
                    if x%i == 0 and y%i==0:
                        return True
                return False
                
        matrix = [ [-1]*len(A) for _ in A]
        for i in range(len(A)):
            for j in range(len(A)):
                if i==j:
                    continue
                matrix[i][j]=commonfactor(A[i],A[j])
        print(matrix)
        visited = [False]*len(A)        
        def dfs(s):
            if visited[s]:
                return
            else:
                visited[s] = True
                for j,n in enumerate(matrix[s]):
                    if n==1 and not visited[j]:
                        dfs(j)
        res = [0]
        for i in xrange(len(A)):
            if not visited[i]:
                dfs(i)
                res.append(sum(visited)-res[-1])
        # print(res)
        return max(res)