#User function Template for python3

class Solution:
    def findIndex(self, arr, x):
        for i in range(len(arr)-1,-1,-1):
            if arr[i]==x:
                return i+1
        return -1
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.findIndex(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends