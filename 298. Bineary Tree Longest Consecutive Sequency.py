# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def recurse_tree(root, cur_m):
            cur_l, cur_r = cur_m, cur_m   
            if root.left is not None:
                if root.left.val == root.val + 1:
                    cur_l +=1
                    max_.append(cur_l)
                    recurse_tree(root.left, cur_l)
                else:
                    recurse_tree(root.left, 1)

            if root.right is not None:
                if root.right.val == root.val + 1:
                    cur_r +=1
                    max_.append(cur_r)
                    recurse_tree(root.right, cur_r)
                else:
                    recurse_tree(root.right, 1)
                 
            max_.append(1)
            return
                
        max_ = []
        recurse_tree(root, 1)
        return max(max_)