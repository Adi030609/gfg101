from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        n=len(adj)
        visit=[False]*n
        q=deque()
        ans=[]
        q.append(0)
        visit[0]=True
        ans.append(0)
        while q:
            val=q.popleft()
            for i in adj[val]:
                if not visit[i]:
                    q.append(i)
                    ans.append(i)
                    visit[i]=True
        return ans
                    
                