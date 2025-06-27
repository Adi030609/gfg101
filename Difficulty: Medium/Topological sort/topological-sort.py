from collections import deque
class Solution:
    
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        indegree = [0] * V
        for edge in edges:
            u, v = edge
            adj[u].append(v)
            indegree[v] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for adj_node in adj[node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    q.append(adj_node)
        
        return ans

