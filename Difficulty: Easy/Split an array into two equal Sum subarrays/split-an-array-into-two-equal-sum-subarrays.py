class Solution:
    def canSplit(self, arr):
        #code here
        prefix=[0]*len(arr)
        prefix[0]=arr[0]
        for i in range(1,len(arr)):
            prefix[i]=arr[i]+prefix[i-1]
        total=prefix[-1]
        for i in range(len(arr)):
            if total-prefix[i]==prefix[i]:
                return True
        return False

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends