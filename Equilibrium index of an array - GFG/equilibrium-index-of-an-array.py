# Your task is to ocomplete this function
# Function should return an integer
def findEquilibrium(a,n):
    # Code here
    sum = []
    s = 0
    for i in a:
        s += i
        sum.append(s)
    
    s = 0
    for i in range(n-1, -1, -1):
        
        if i > 0 and sum[i-1] == s:
            return i
        s += a[i]
    
    return -1


#{ 
#  Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(findEquilibrium(arr,n))
# Contributed By: Harshit Sidhwa

# } Driver Code Ends