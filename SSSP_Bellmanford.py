def bellman_ford(adj_matrix, source):
    vertices = len(adj_matrix)
    dist = [float('inf')] * vertices
    dist[source] = 0
    for _ in range(vertices - 1):
        print("\n\nRelation iteration ",_+1,":")
        for u in range(vertices):
            for v in range(vertices):
                if adj_matrix[u][v] != 0:
                    if dist[u] + adj_matrix[u][v] < dist[v]:
                        dist[v] = dist[u] + adj_matrix[u][v]
                    print("After relaxation of (",u+1,",",v+1,") edge: ",dist)
    for u in range(vertices):
        for v in range(vertices):
            if adj_matrix[u][v] != 0:
                if dist[u] + adj_matrix[u][v] < dist[v]:
                    raise ValueError("Graph contains a negative cycle")

    return dist
N=int(input("Enter no of vertices:"))
G=[]
print("Enter adjacency matrix:")
for _ in range(N):
    row=list(map(int,input().split()))
    G.append(row)
source_vertex = int(input("Enter Source Vertex:"))
result = bellman_ford(G, source_vertex)
for i in range(len(result)):
        print(f"Vertex {i + 1}: Distance = {result[i]}")


