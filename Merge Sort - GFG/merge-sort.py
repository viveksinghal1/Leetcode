#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        
        n1 = m - l + 1
        n2 = r - m
        L = [arr[l+i] for i in range(n1)]
        R = [arr[m+1+j] for j in range(n2)]
        i, j = 0, 0
        k = l
        
        while i < n1 and j < n2:
            
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            
            k += 1
            
        while i < n1:
            
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < n2:
            
            arr[k] = R[j]
            j += 1
            k += 1
            
            
    def mergeSort(self,arr, l, r):
        #code here
        
        if l < r:
            
            mid = (l+r)//2
            
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid+1, r)
            self.merge(arr, l, mid, r)


#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends