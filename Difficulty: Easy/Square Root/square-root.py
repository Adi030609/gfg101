#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, n):
        l=1
        h=n
        ans=0
        while l<=h:
            mid=(l+h)//2
            if mid**2==n:
                return mid
            if mid**2>n:
                h=mid-1
            else:
                l=mid+1
                ans=mid
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends