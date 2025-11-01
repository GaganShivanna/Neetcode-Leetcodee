class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = collections.defaultdict(list)
        for i in range(n):
            if manager[i]!= -1:
                adj[manager[i]].append(i)
        
        q = deque([(headID, 0)]) # Id, Time
        res = 0 
        while q:
            id, time = q.popleft()
            res = max(res, time)
            for emp in adj[id]:
                q.append((emp, time + informTime[id]))
        return res

