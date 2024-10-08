class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        res = []
        i = 0
        j = 0
        
        while i < m and j < n:
            
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            
            elif nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
                
            else:
                res.append(nums1[i])                
                res.append(nums1[i])
                i += 1
                j += 1
                
        # print(res)
        
        while i < m:
            res.append(nums1[i])
            i += 1
            
        while j < n:
            res.append(nums2[j])
            j += 1
                
        for i in range(m+n):
            nums1[i] = res[i]