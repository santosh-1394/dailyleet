# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        from collections import deque, defaultdict

        
        parent = {}
        def dfs(node, par=None):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root)

        
        queue = deque([(target, 0)])
        seen = {target}
        result = []

        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.val)
            elif dist < k:
                for nei in (node.left, node.right, parent[node]):
                    if nei and nei not in seen:
                        seen.add(nei)
                        queue.append((nei, dist + 1))
        
        return result
