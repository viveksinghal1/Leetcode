class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        
        if length == 1:
            return
        
        i = length - 2
        while i >=0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            j = length - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
            
        # print(nums)
        self.reverse(nums, i+1, length - 1)
    
    def swap(self, nums: List[int], i: int, j: int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def reverse(self, nums: List[int], i: int, j:int) -> None:
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1