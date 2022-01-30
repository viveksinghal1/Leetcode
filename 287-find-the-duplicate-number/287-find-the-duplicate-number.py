class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) TC and O(n) SC
        
        n = len(nums)
        flagArray = [False]*(n)
        
        for i in nums:
            
            if flagArray[i]:
                return i
            else:
                flagArray[i] = True