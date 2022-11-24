class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ''' TC -> O(N+E) (for iterating all vertices and adding edges) + O(NlogN) (for heap operation {logN} for all vertices -> N * logN)
        SC -> O(V+E) + O(2N)
        '''
        
        n = len(points)
        adj = [[] for i in range(n)]
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2) # manhatten distance
                adj[i].append([dist, j])
                adj[j].append([dist, i])
                
        # Prim's Algorithm
        
        visit = set()
        totalCost = 0
        minH = [[0, 0]]
        
        while len(visit) < n:
            cost, u = heapq.heappop(minH)
            if u in visit:
                continue
            totalCost += cost    
            visit.add(u)
            
            for vCost, v in adj[u]:
                if v not in visit:
                    heapq.heappush(minH, [vCost, v])
                    
        return totalCost
                