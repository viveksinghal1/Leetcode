class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, max = 0, -10000
            
        length = len(nums)
        for i in range(0, length):
            sum += nums[i]
            
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
                
        return max
                
        