# User function Template for python3

class Solution:
   def equalSum(self, arr):
        if len(arr) == 0:
            return -1  
        if len(arr) == 1:
            return 0 
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        for i in range(1, len(arr)):
            prefix[i] = arr[i] + prefix[i - 1]
        
        total = prefix[-1]
        for i in range(len(arr)):
            leftsum = prefix[i] - arr[i]
            rightsum = total - prefix[i]
            
            if leftsum == rightsum:
                return i
        
        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.equalSum(arr))

        T -= 1
        print("~")

# } Driver Code Ends