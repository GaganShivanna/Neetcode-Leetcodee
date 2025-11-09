class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n =len(bombs)

        #Step 1: Building the directed graph by making use of adjacency list 
        graph = [[] for _ in range(n)]
        for i in range(n):
            xi, yi, ri = bombs[i]
            radius = ri * ri 
            for j in range(n):
                if i == j:
                    continue
                xj, yj, rj = bombs[j]
                dx,dy = xi - xj, yi - yj 
                if dx * dx + dy * dy <= radius : 
                    graph[i].append(j)

        #Step 2: Run the DFS traversal to find all the bombs that are reachable to detonate 

        def dfs(node, visited):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, visited)

        #step 3 : Trying to detonate the Maximum Bomb 
        maxDetonate = 0 
        for i in range(n):
            visited = set()
            dfs(i, visited)
            maxDetonate = max(maxDetonate, len(visited)) 

        return maxDetonate 