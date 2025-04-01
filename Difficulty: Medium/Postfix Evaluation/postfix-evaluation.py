#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends


class Solution:
    def evaluate(self, arr):
        def isinteger(n):
            try:
                int(n)
                return True
            except ValueError:
                return False
        stack=[]
        for i in arr:
            if isinteger(i):
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
        
                if i == "*":
                    stack.append(a * b)
                elif i == "/":
                    stack.append(int(a / b))
                elif i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
        
        return stack[0] if stack else 0

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = input().split()
        solution = Solution()
        print(solution.evaluate(arr))
        print("~")

# } Driver Code Ends