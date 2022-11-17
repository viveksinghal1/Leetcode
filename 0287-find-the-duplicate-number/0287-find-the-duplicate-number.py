class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) TC and O(1) SC
        
        slow = 0
        fast = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        fast = 0
        
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
            
        return slow
        
        
            