class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        trackElementsMap = dict()
        maxLength = 0
        
        for num in nums:
            trackElementsMap[num] = True
        
        for num in nums:
            if (num-1) in trackElementsMap:
                continue
            else:
                count = 1
                temp = num
                while (num + 1) in trackElementsMap:
                    count += 1
                    num += 1
                if count > maxLength:
                    maxLength = count
                    
        return maxLength