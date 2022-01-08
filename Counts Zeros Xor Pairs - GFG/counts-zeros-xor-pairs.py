#User function Template for python3


def calculate (arr, n) : 
    #Complete the function
    duplicates = {}
    count = 0
    
    for i in range(n):
        if arr[i] in duplicates.keys():
            count += duplicates[arr[i]]
            c = duplicates[arr[i]] + 1
            duplicates.update({arr[i]: c})
        else:
            duplicates[arr[i]] = 1
            
    return count


#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = calculate(arr, n)
    print(res)


# } Driver Code Ends