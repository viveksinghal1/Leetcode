import heapq

class Solution:
	def topK(self, nums, k):
		#Code here
		# O(klogn) + O(n) sol using heap
		
		freqArr = dict()
		
		for i in nums:
		    if i in freqArr:
		        freqArr[i] += 1
		    else:
		        freqArr[i] = 1
		 
		heap = [(value, key) for key, value in freqArr.items()]
		
		
		klargest = heapq.nlargest(k, heap)
		
		result = [j for (i,j) in klargest]
		
		return result
		  

#{ 
#  Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
# } Driver Code Ends