class Solution:
    def count(self, coins, sum):
        mapp = {}
        def recur(coins, n, sum):
            if (n, sum) in mapp:
                return mapp[(n, sum)]
            if sum == 0:
                return 1
            if sum < 0 or n == 0:
                return 0
            mapp[(n, sum)]=recur(coins, n, sum-coins[n-1])+recur(coins, n-1, sum)
            return mapp[(n, sum)]
        return recur(coins, len(coins), sum)