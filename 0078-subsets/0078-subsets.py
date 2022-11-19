class Solution:
    
    def dfs(self, nums, res, ds, i):
        res.append(ds[:])
        
        for ind in range(i, len(nums)):
            ds.append(nums[ind])
            self.dfs(nums, res, ds, ind+1)
            ds.pop()
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # TC -> O(2^N), SC -> O(2^N)
        res = []
        self.dfs(nums, res, [], 0)
        return res