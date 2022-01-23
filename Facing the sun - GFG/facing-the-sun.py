#User function Template for python3
class Solution:
    
    def countBuildings(self,h, n):
        # code here
        maxHeight = -1
        count = 0
        
        for i in h:
            if i > maxHeight:
                count += 1
                maxHeight = i
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        h = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(h, n)
        print(ans)
        tc -= 1

# } Driver Code Ends