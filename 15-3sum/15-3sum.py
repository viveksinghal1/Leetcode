class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        
        nums.sort()
        
        for i in range(n):
            if i == 0 or ( nums[i] != nums[i-1]):
                front, end = i + 1, n-1
                while front < end:
                    s = nums[front] + nums[end]
                    if s < (-nums[i]):
                        front += 1
                    elif s > (-nums[i]):
                        end -= 1
                    else:
                        res.append([nums[i], nums[front], nums[end]])
                        
                        while front < end and nums[front] == res[-1][1]:
                            front += 1
                        while front < end and nums[front] == res[-1][2]:
                            end -= 1
            
        return res 