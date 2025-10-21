"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return 
        q = deque([root])
        res = []

        while q:
            level = []
            for _ in range(len(q)):
                n = q.popleft()
                level.append(n.val)
                for c in n.children:
                    q.append(c)
            res.append(level)
        return res
        