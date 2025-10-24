class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c : [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        cycle, visited = set(), set()
        output = []
        def dfs(crs):
            if crs in cycle: 
                return False
            if crs in visited:
                return True 
            cycle.add(crs)

            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output