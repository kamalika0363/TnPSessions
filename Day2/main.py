def solution(lst, x, y):
    def rec(pos, curr_cost, count):
        if pos >= len(lst) and count == 0:
            return curr_cost

        if pos >= len(lst) or count == 0:
            return float('inf')

        curr = rec(pos + y, lst[pos] + curr_cost, count - 1)
        skip_curr = rec(pos + 1, 0, x)

        return min(curr, skip_curr)

    return rec(0, 0, x)






def dfs(v, graph, removed):
    if v in removed:
        return 0
    
    removed.add(v)
    count = 1
    
    for u in graph[v]:
        count += dfs(u, graph, removed)
    
    return count

def solution(N, A, B):
    graph = [[] for _ in range(N)]
    
    for i in range(len(A)):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])
    
    seconds = 0
    removed = set()
    
    while len(removed) < N:
        to_remove = set()
        
        for v in range(N):
            if v not in removed and len(graph[v]) <= 1:
                to_remove.add(v)
        
        for v in to_remove:
            removed.add(v)
            
            for u in graph[v]:
                graph[u].remove(v)
        
        if to_remove:
            seconds += 1
        else:
            break
    
    return seconds

