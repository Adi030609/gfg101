#User function Template for python3

class Solution:
    def countZeroes(self, arr):
        count=0
        l=len(arr)-1
        for i in range(l,-1,-1):
            if arr[i]==0:
                count += 1
            else:
                break
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countZeroes(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends