#User function Template for python3

class Solution:
    def segregate0and1(self, arr, n):
        # code here
        s = sum(arr)
        
        for i in range(n-s):
            arr[i] = 0
        for i in range(n-s, n):
            arr[i] = 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregate0and1(arr, n)
        print(*arr)
        tc -= 1

# } Driver Code Ends