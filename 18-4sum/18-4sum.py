class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        n = len(nums)
        
        # not using range function here in iteration because range updates i/j one by one
        # and i/j doesn't get changed by duplicates checking loops
        
        nums.sort()
        i = 0
        while i < n:
            target_i = target - nums[i]
            j = i + 1
            while j < n:
                target_j = target_i - nums[j]
                
                front, end = j+1, n-1
                
                while front < end:
                    two_sum = nums[front] + nums[end]
                    
                    if two_sum < target_j:
                        front += 1
                    elif two_sum > target_j:
                        end -= 1
                    else:
                        res.append([nums[i], nums[j], nums[front], nums[end]])
                        while front < end and nums[front] == res[-1][2]:
                            front += 1
                        while front < end and nums[end] == res[-1][3]:
                            end -= 1
                            
                while j + 1 < n and nums[j] == nums[j+1]:
                    j += 1
                j += 1
            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            i += 1
                
        return res