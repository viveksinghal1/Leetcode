// { Driver Code Starts
import java.util.*;

class Count
{
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            int m = sc.nextInt();
            int n = sc.nextInt();
            
            int arr1[] = new int[m];
            int arr2[] = new int[n];
            
            for(int i = 0; i < m; i++)
              arr1[i] = sc.nextInt();
              
            for(int i = 0; i < n; i++)
              arr2[i] = sc.nextInt();
              
            Solution gfg = new Solution();
            ArrayList<Integer> res = gfg.countEleLessThanOrEqual(arr1, arr2, m, n);
            for (int i = 0; i < res.size(); i++)
                System.out.print (res.get (i) + " ");
            System.out.println();
        }
        
    }
}// } Driver Code Ends


// Complete the function given below
class Solution
{
    
    static int bin_search(int key, int arr[], int n) {
        int l = 0;
        int h = n - 1;
        
        while (l <= h) {
            int mid = (l + h) / 2;
            
            if (arr[mid] <= key) {
                l = mid + 1;
            } else {
                h = mid - 1;
            }
            
        }
        
        return h+1;
    }
    
    public static ArrayList<Integer> countEleLessThanOrEqual(int arr1[], int arr2[], int m, int n)
    {
       // add your code here
       ArrayList<Integer> res = new ArrayList<>();
       Arrays.sort(arr2);
       
       for (int i = 0; i < m; i++) {
           res.add(bin_search(arr1[i], arr2, n));
       }
       
       return res;
    }
}