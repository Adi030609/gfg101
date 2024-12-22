#User function Template for python3

class Solution:
    # Function to find the length of the longest common subsequence in two strings.
    def getLCSLength(self, s1, s2):
        m=len(s1)
        n=len(s2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]
            


#{ 
 # Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s1 = str(input())  # Take first string as input
        s2 = str(input())  # Take second string as input
        ob = Solution()
        # Call the getLCSLength function and print the result
        print(ob.getLCSLength(s1, s2))
        print("~")
# } Driver Code Ends