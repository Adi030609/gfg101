#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        n=len(cost)
        dp=[0]*(n+1)
        for i in range(2,n+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[n]
        


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends