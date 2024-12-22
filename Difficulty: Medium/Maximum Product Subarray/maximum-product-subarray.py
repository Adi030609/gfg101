#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
	    if not arr:
            return 0

        # Initialize variables
        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]

        # Traverse the array
        for i in range(1, len(arr)):
            current = arr[i]
            
            # If current number is negative, swap max and min
            if current < 0:
                max_product, min_product = min_product, max_product

            # Update max and min products
            max_product = max(current, max_product * current)
            min_product = min(current, min_product * current)

            # Update the result with the maximum product found so far
            result = max(result, max_product)

        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends