# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)

        def dfs(node):
            if not node:
                return
            if node.left: 
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        q = deque([start])
        max_time = -1
        visited = set()

        while q: 
            max_time += 1
            for _ in range(len(q)):
                node= q.popleft()
                visited.add(node)
                for nei in adj[node]:
                    if nei not in visited:
                        q.append(nei)

        return max_time