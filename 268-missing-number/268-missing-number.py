class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = 0
        lnt = len(nums)
        for i in range(lnt):
            res ^= (i+1)^(nums[i])
            
        return res