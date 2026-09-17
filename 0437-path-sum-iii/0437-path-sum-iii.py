# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return 0

        # Paths starting from this node
        count = self.findPaths(root, targetSum)

        # Try starting a path from left and right children
        count += self.pathSum(root.left, targetSum)
        count += self.pathSum(root.right, targetSum)

        return count

    def findPaths(self, node, target):
        if not node:
            return 0

        count = 0

        if node.val == target:
            count += 1

        count += self.findPaths(node.left, target - node.val)
        count += self.findPaths(node.right, target - node.val)

        return count