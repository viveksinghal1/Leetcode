#User function Template for python3

class Solution:
	def swapElements(self, arr, n):
		#Code here
		if len(arr) < 3:
		    return
		if len(arr) % 2 == 0:
		    arr.append(arr[0])
		    arr.append(arr[1])
		else:
		    arr.append(arr[1])
	    	arr.append(arr[0])    
		arr.pop(0)
		arr.pop(0)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
    	obj = Solution()
    	obj.swapElements(arr, n);
    	for i in arr:
    	    print(i, end = " ")
    	print()
# } Driver Code Ends