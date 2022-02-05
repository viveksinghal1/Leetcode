#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        
        maxLength = 0
        sum = 0
        
        m = dict()
        
        for i in range(n):
            sum += arr[i]
            if sum == 0:
                maxLength = i + 1
            else:
                if sum in m:
                    if (i-m[sum]) > maxLength:
                        maxLength = (i-m[sum])
                else:
                    m[sum] = i
        return maxLength

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends