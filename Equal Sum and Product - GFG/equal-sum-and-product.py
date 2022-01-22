#User function Template for python3
class Solution:

	
	def numOfsubarrays(self,arr, n):
    	# code here
    	count = 0
    	
    	for i in range(n):
    	    sum = arr[i]
    	    prod = arr[i]
    	    count += 1
    	    for j in range(i+1, n):
    	        sum += arr[j]
    	        prod *= arr[j]
    	        if sum == prod:
    	            count += 1
    	            
    	return count



#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.numOfsubarrays(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends