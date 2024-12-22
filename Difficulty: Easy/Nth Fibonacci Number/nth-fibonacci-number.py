
class Solution:
    def nthFibonacci(self, n: int) -> int:
        memo={}
        def fib(n):
            if n<=1:
                return n
            if n in memo:
                return memo[n]
            memo[n]=fib(n-1)+fib(n-2)
            return memo[n]
        return fib(n)
            
        



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