#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
	    n=len(arr)
	    dp=[[0]*(target+1) for _ in range(n+1)]
	    dp[0][0]=1
	    for i in range(1,n+1):
	        for j in range(target+1):
	            dp[i][j]=dp[i-1][j]
	            if j>=arr[i-1]:
	                dp[i][j]+=dp[i-1][j-arr[i-1]]
        return dp[n][target]
	        