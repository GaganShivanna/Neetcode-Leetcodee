"""
# Definition for a Node.
class Node:
    def __init__(self, neighbors = None, val= 0):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            clone = Node(node.val)
            oldToNew[node]= clone 

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone 

        return dfs(node) if node else None