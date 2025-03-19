#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        sec = float("-inf")
        maxx = float("-inf")
        for i in range(len(arr)):
            if arr[i] > maxx:
                sec = maxx 
                maxx = arr[i]  
            elif arr[i] > sec and arr[i] != maxx:
                sec = arr[i]
        
        if sec == float("-inf"):
            return -1 
        else:
            return sec 

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends