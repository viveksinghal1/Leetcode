class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) TC and O(1) SC
        
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
        
        
            