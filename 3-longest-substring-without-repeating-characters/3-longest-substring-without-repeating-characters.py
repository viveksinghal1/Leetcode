class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        
        unique = dict()
        longest = 0
        start = 0
        
        for i in range(n):
            if s[i] in unique:
                start = max(start, unique[s[i]] + 1)
            longest = max(longest, i-start+1)
            unique[s[i]] = i
            
        return longest