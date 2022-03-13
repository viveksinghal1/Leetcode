class Solution:
    
    def findSubset(self, nums, res, ds, index, n) -> None:
        
        if index >= n:
            res.append(ds[:])
            return
        
        self.findSubset(nums, res, ds, index+1, n)
        ds.append(nums[index])
        self.findSubset(nums, res, ds, index+1, n)
        ds.pop()
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        self.findSubset(nums, res, [], 0, n)
        return res
        