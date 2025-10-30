class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycle, visited = set(), set()
        output = []

        def dfs(crs):
            if crs in cycle: 
                return False
            if crs in visited:
                return True 
            cycle.add(crs)

            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return output 
            

