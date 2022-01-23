#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        
        largestSize = 0
        sum = 0
        
        sumAtIndeces = dict();
        
        for i in range(n):
            sum += arr[i]
            
            if sum == 0:
                if (i+1) > largestSize:
                    largestSize = i+1
            else:
                if sum in sumAtIndeces:
                    length = i - sumAtIndeces[sum]
                    if length > largestSize:
                        largestSize = length
                        # print(sumAtIndeces[sum], i)
                
                if sum not in sumAtIndeces:
                    sumAtIndeces[sum] = i
            
            # sumAtIndeces[sum] = i        
            # print(sumAtIndeces)
                    
        return largestSize

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