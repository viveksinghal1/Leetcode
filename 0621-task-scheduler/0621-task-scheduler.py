class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # TC -> O(N), SC -> O(26)
        count = [0]*26
        
        for task in tasks:
            count[ord(task)-ord("A")] += 1
        
        count.sort()
        i = 25
        '''here decreasing to the element which has same frequency as most frequent element. eg: AABBC -> here A and B has same most frequency''' 
        while i >= 0 and count[i] == count[25]:
            i -= 1
        
        '''here tasks length will be maximum if distinct tasks frame length is greater than n. eg: AABBCCD, n=1 => ABCDABC
        otherwise its tasks length + idle time which is calculated as
        (count[25]-1)*n + count[25] + (25-i-1) where (count[25]-1)*n is number of slots in frame (AXXXAXXXA), 2nd term count[25] is time taken by most frequent element itself (no of A) and 3rd term (25-i-1) is the number that has to be added behind the last frame (eg ABXXABXXAB, in here we have to add 1 B which (25-23-1))'''
        
        return max(len(tasks), (count[25]-1)*(n+1)+25-i)