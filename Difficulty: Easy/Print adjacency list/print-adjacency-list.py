
from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        adj=[[] for _ in range(V)]
        def addedge(adj,v,u):
            adj[u].append(v)
            adj[v].append(u)
        for i in range(len(edges)):
            addedge(adj,edges[i][0],edges[i][1])
        return adj
        