# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not subRoot:
            return True
        if not root:
            return False

        def isSameTree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return (s.val == t.val and 
                    isSameTree(s.left, t.left) and 
                    isSameTree(s.right, t.right))

        
        return (isSameTree(root, subRoot) or 
                self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
