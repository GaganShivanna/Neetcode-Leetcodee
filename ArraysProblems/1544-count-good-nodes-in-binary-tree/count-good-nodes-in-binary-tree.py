# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        q= deque([(root,root.val)])
        count = 0

        while q:
            node, max_so_far = q.popleft()
            if node.val >= max_so_far:
                count +=1
                
            new_max = max(max_so_far, node.val)

            if node.left:
                q.append((node.left, new_max))
            if node.right:
                q.append((node.right, new_max))
        return count 