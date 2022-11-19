class Solution:
    
    def find(self, par, n):
        p = par[n]
        
        # while p != par[p]:
        #     par[p] = par[par[p]]
        #     p = par[p]
        if p != par[p]:
            p = par[p] = self.find(par, p)
        return p
    
    def union(self, par, rank, n1, n2):
        p1, p2 = self.find(par, n1), self.find(par, n2)
        
        if p1 == p2:
            return False
        
        if rank[p1] > rank[p2]:
            par[p2] = p1
            rank[p1] += 1
        else:
            par[p1] = p2
            rank[p2] += 1
        
        return True
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # TC -> O(N) * 4*alpha, SC -> O(N)
        
        par = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)
        
        for n1, n2 in edges:
            if not self.union(par, rank, n1, n2):
                return [n1, n2]
        
        return []