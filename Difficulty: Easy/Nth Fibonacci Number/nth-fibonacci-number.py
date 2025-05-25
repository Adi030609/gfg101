
class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n<=1:
            return n
        dp=[0]*(n+1)
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
            
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.nthFibonacci(n)

        print(res)

        print("~")

# } Driver Code Ends