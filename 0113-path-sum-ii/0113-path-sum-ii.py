# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(node, path, remaining):
            if not node:
                return
            
            
            path.append(node.val)
            
            
            if not node.left and not node.right and remaining == node.val:
                result.append(list(path))
            else:
                
                dfs(node.left, path, remaining - node.val)
                dfs(node.right, path, remaining - node.val)
            
            
            path.pop()

        dfs(root, [], targetSum)
        return result
