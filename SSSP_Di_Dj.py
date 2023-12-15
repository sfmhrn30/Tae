import heapq
def dijkstra(graph, start):
    num_vertices = len(graph)
    distance = [float('inf')] * num_vertices
    predecessor = [None] * num_vertices
    visited = [False] * num_vertices
    distance[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        dist_u, u = heapq.heappop(priority_queue)
        if visited[u]:
            continue
        visited[u] = True
        for v, weight in enumerate(graph[u]):
            if not visited[v] and weight != 0:
                new_distance = distance[u] + weight

                if new_distance < distance[v]:
                    distance[v] = new_distance
                    predecessor[v] = u
                    heapq.heappush(priority_queue, (distance[v], v))
    return distance, predecessor
def print_results(distance, predecessor, start,j):
    print(f"Vertex {j + 1}: Shortest Distance = {distance[j]}, Predecessor = {predecessor[j] + 1 if predecessor[j] is not None else None}")
    print(f"\nShortest Paths from Vertex {start + 1} to {j} vertex:")
    path = [j + 1]
    current = j
    while predecessor[current] is not None:
        path.insert(0, predecessor[current] + 1)
        current = predecessor[current]
    print(f"To Vertex {j + 1}: {path}")
n = int(input("Enter the number of vertices: "))
start_vertex = int(input("Enter the start vertex (1 to N): ")) - 1
graph=[]
print("Enter adjacency matrix:")
for _ in range(n):
    row=list(map(int,input().split()))
    graph.append(row)
print("\nGraph:")
for row in graph:
        print(row)
distances, predecessors = dijkstra(graph, start_vertex)
j=int(input("Enter vertex j:"))
print_results(distances, predecessors, start_vertex,j)
