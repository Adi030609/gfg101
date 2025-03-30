#User function Template for python3
class Solution:
    
    def findSplit(self, arr):
        res = []
        total = 0
        
        for ele in arr:
            total += ele
        if total % 3 != 0:
            res = [-1, -1]
            return res
        currSum = 0
        
        for i in range(len(arr)):
            currSum += arr[i]
            if currSum == total / 3:
                currSum = 0
                res.append(i)

                if len(res) == 2 and i < len(arr) - 1:
                    return res
        res = [-1, -1]
        return res

#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if (result == [-1, -1]) or len(result) != 2:
            print("false")

        else:
            sum1 = sum2 = sum3 = 0
            for i in range(len(arr)):
                if i <= result[0]:
                    sum1 += arr[i]
                elif i <= result[1]:
                    sum2 += arr[i]
                else:
                    sum3 += arr[i]

            if sum1 == sum2 == sum3:
                print("true")
            else:
                print("false")
        print("~")
# } Driver Code Ends