# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        def dfs_leftbound(root, res):
            if not root or (not root.left and not root.right):
                return
            res.append(root.val)
            if root.left:
                dfs_leftbound(root.left, res)
            else:
                dfs_leftbound(root.right, res)
                
        def dfs_rightbound(root, res):
            if not root or (not root.left and not root.right):
                return
            if root.right:
                dfs_rightbound(root.right, res)
            else:
                dfs_rightbound(root.left, res)
            res.append(root.val)
                
        def leaf(root, res):
            if not root:
                return
            if not root.left and not root.right:
                res.append(root.val)
            leaf(root.left, res)
            leaf(root.right, res)    
            
        if root.left or root.right:
            res = [root.val]
        else:
            res = []
        
        dfs_leftbound(root.left,res)
        leaf(root, res)
        dfs_rightbound(root.right, res)
        return res
                
                

        
            
        