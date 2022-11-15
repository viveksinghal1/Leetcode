class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # TC -> O(N), SC -> O(1)
        
        l, h = 0, len(numbers)-1
        
        while l < h:
            s = numbers[l] + numbers[h]
            if s == target:
                return [l+1, h+1]
            if s > target:
                h -= 1
            else:
                l += 1
        
        return -1