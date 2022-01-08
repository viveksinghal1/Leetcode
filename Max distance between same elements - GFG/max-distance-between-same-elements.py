class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr, n):
        # Code here
        elements = {}
        maxDist = 0
        
        for i in range(n):
            if arr[i] in elements:
                if (i - elements[arr[i]]) > maxDist:
                    maxDist = i - elements[arr[i]]
            else:
                elements[arr[i]] = i
        return maxDist


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.maxDistance(arr, n))
# Contrbuted By:Harshit Sidhwa


# } Driver Code Ends