class Solution:
    # Returns shortest distances from src to all other vertices
    
    def dijkstra(self, v, edges, src):
        def constructadj(edges,v):
            adj=[[] for _ in range(v)]
            for e in edges:
                u,v,cost=e
                adj[u].append([v,cost])
                adj[v].append([u,cost])
            return adj
        adj=constructadj(edges,v)
        pq=[]
        dis=[float("inf")]*(v)
        heapq.heappush(pq,[0,src])
        dis[src]=0
        while pq:
            u=heapq.heappop(pq)[1]
            for x in adj[u]:
                v,wt=x[0],x[1]
                if dis[v]>dis[u]+wt:
                    dis[v]=dis[u]+wt
                    heapq.heappush(pq,[dis[v],v])
        return dis
        