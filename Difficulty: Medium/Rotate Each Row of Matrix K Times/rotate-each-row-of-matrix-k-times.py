class Solution:
    def rotateMatrix(self, k, mat):
        r, c = len(mat), len(mat[0])
        k = k % c
        new = [[0] * c for _ in range(r)]
    
        for i in range(r):
            for j in range(c):
                new[i][j - k] = mat[i][j]
    
        return new


#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends