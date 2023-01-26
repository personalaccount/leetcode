'''
There are n cities connected by some number of flights. 
You are given an array flights where 
flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
If there is no such route, return -1.

'''

import heapq

def findCheapestPrice(n: int, flights, src: int, dst: int, k: int) -> int:
    graph = [[] for _ in range(n)]
    for f in flights:
        graph[f[0]].append((f[1], f[2]))
    
    heap = [(0, src, k+1)]
    while heap:
        p, i, k = heapq.heappop(heap)
        if i == dst:
            return p
        if k > 0:
            for j, w in graph[i]:
                heapq.heappush(heap, (p+w, j, k-1))
    return -1

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

print(findCheapestPrice(n, flights, src, dst, k))
