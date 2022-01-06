#User function Template for python3
from functools import reduce

class Solution:
    def isPossible(self, N, arr):
        # code here
        return 1 if (reduce(lambda a,b: a+b, arr, 0) % 3 == 0) else 0
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code Ends