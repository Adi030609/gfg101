#User function Template for python3

class Solution:
    def maxStep(self, arr):
        i,j = 0,1
        currentCount=0
        maxCount=0
        if not arr:
            return 0
        while i<len(arr)-1:
            if arr[i]<arr[j]:
                currentCount += 1
                i += 1
                j += 1
                if maxCount<currentCount:
                    maxCount=currentCount
            else:
                currentCount=0
                i += 1
                j += 1
        return maxCount
        
          
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends