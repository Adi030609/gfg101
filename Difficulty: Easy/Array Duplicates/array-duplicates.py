
from typing import List


class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        s = set()
        d = set()
        for num in arr:
            if num not in s:
                s.add(num)
            else:
                d.add(num)
        if not d: 
            return [-1]  
        else:
            return sorted(list(d)) 
            
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.duplicates(n, arr)

        IntArray().Print(res)

# } Driver Code Ends