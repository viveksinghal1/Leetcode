class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        currMax = 1
        currMin = 1
        for num in nums:
            temp = currMax*num
            currMax = max(num*currMax, num*currMin, num)
            currMin = min(temp, num*currMin, num)
            maxi = max(maxi, currMax)
        
        return maxi