def floyd_warshall_with_paths(adj_matrix):
    n = len(adj_matrix)
    dist = [row[:] for row in adj_matrix]
    pred = [[None if i != j and adj_matrix[i][j] != float('inf') else -1 for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = k
    for i in range(n):
        print(f"Shortest paths from vertex {i}:")
        for j in range(n):
            if i != j :
                path=[j]
                path = reconstruct_path(pred, i, j,path)
                print(f"To vertex {j}: {path}")
def reconstruct_path(pred, start, end,path):
    if pred[start][end]==None:
        path.insert(0,start)
        return path
    if pred[start][end] != -1:
        j = pred[start][end]
        path.insert(0, j)
        reconstruct_path(pred,start,j,path)
    return path

n = int(input("Enter the number of vertices: "))
graph = []

print("Enter the adjacency matrix for the graph (Enter INF for infinity):")
for i in range(n):
    row = []
    for j in range(n):
        weight = float('inf') if i == j else float(input(f"Enter weight from vertex {i+1} to {j+1}: "))
        row.append(weight)
    graph.append(row)
floyd_warshall_with_paths(graph)
