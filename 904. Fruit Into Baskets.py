class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        import collections
        count = collections.Counter()
        ans,i=0,0
        for j,x in enumerate(tree):
            count[x]+=1
            while len(count)>=3:
                count[tree[i]]-=1
                if count[tree[i]]==0:
                    del count[tree[i]]
                i+=1
            ans = max(j-i+1, ans)
        return ans