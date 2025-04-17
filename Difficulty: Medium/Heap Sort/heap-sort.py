#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def heapSort(self, arr):
        #code here
        arr.sort()

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.heapSort(arr)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends