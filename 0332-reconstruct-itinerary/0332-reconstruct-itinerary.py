from collections import deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # TC -> O((V+E)^2) ~ O(E^2) bcz is E ~ V in this question
        # SC -> O(E)
        
        adj = {u: deque() for u, v in tickets}
        res = ["JFK"]
        tickets.sort()
        for u, v in tickets:
            adj[u].append(v)
            
        def dfs(curr):
            if len(res) == len(tickets)+1:
                return True
            if curr not in adj:
                return False
            
            temp = list(adj[curr])
            for v in temp:
                adj[curr].popleft()
                res.append(v)
                if dfs(v):
                    return True
                res.pop()
                adj[curr].append(v)
                
            return False
                
        dfs("JFK")
        return res