class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        ans=[]
        n=len(adj)
        visit=[False]*n
        def findpath(s,ans):
            visit[s]=True
            ans.append(s)
            for i in adj[s]:
                if not visit[i]:
                    findpath(i,ans)
            return ans
        findpath(0,ans)
        return ans