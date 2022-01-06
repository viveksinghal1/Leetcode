#User function Template for python3
from functools import reduce

def sumElement(arr,n):
    #code here
    return reduce(lambda a, b: a+b, arr, 0)
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    testCase=int(input())
    
    for _ in range(testCase):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        print(sumElement(arr,n))
# } Driver Code Ends