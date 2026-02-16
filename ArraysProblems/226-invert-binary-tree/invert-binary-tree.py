# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return 
        stack = [root]
        while stack: 
            nodes = stack.pop()
            nodes.left, nodes.right = nodes.right, nodes.left
            if nodes.left:
                stack.append(nodes.left)
            if nodes.right:
                stack.append(nodes.right)
        return root 