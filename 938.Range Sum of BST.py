# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root is None:
            return 
        q=[root]
        s=[]
        while len(q)>0:
            for node in q:
                if node.val>=min(L,R) and node.val<=max(L,R):
                    s.append(node.val)
            next_q =[]
            for node in q:
                if node.left is not None:
                    next_q.append(node.left)
                if node.right is not None:
                    next_q.append(node.right)
            q= next_q
        return sum(s)