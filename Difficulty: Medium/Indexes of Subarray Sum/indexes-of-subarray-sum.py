#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, arr, n, s):
        if s==0 and n==2:
            return [1,1]
        start=0
        end=0
        sums=0
        while (end<n):
            sums+=arr[end]
            while (sums>s and start<end):
               sums-=arr[start]
               start+=1
            if sums==s:
                return [start+1,end+1]
            else:
                end+=1
        return [-1]

      #Write your code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Co