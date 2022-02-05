class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        trackElementsSet = set(nums)
        maxLength = 0
        
        for num in nums:
            if (num-1) in trackElementsSet:
                continue
            count = 1
            while (num + count) in trackElementsSet:
                count += 1
            maxLength = max(maxLength, count)    
                    
        return maxLength