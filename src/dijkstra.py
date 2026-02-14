import math

def dijkstra_simple(graph, start, end):
    
    distances = {}      # فاصله از مبدأ
    previous = {}       # گره قبلی در مسیر
    visited = {}        # دیده شده‌ها
    nodes = list(graph.keys())

    for node in nodes:
        distances[node] = math.inf
        previous[node] = None
        visited[node] = False
    
    distances[start] = 0
    
    for _ in range(len(nodes)):
        min_dist = math.inf
        min_node = None
        for node in nodes:
            if not visited[node] and distances[node] < min_dist:
                min_dist = distances[node]
                min_node = node
        
        if min_node is None:
            break
        
        visited[min_node] = True
        
        if min_node == end:
            break
    
        for neighbor, weight in graph[min_node].items():
            if not visited[neighbor]:
                new_dist = distances[min_node] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = min_node
    
    if distances[end] == math.inf:
        return None  # مسیر وجود ندارد
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    
    path.reverse()
    return path, distances[end]