#User function Template for python3
class Solution:
    def maxSubstring(self, s):
        if not s:
            return -1
        transformed = [1 if c == '0' else -1 for c in s]
        max_current = max_global = transformed[0]
        for num in transformed[1:]:
            max_current = max(num, max_current + num)
            max_global = max(max_global, max_current)
        return max_global if max_global > 0 else -1

		     
		

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.maxSubstring(s)
        print(answer)
        print("~")

# } Driver Code Ends