def kruskal_algo(n, graph):
    def find(component):
        if parent[component] == component:
            return component
        temp = find(parent[component])
        parent[component] = temp
        return temp
    def union(vertex1, vertex2):
        parent_of_vertex1 = find(vertex1)
        parent_of_vertex2 = find(vertex2)
        if parent_of_vertex1 == parent_of_vertex2:
            return True
        if rank[parent_of_vertex1] > rank[parent_of_vertex2]:
            parent[parent_of_vertex2] = parent_of_vertex1
        elif rank[parent_of_vertex1] < rank[parent_of_vertex2]:
            parent[parent_of_vertex1] = parent_of_vertex2
        else:
            parent[parent_of_vertex1] = parent_of_vertex2
            rank[parent_of_vertex2] += 1
        return False
    print("Minimum Spanning Tree is :-")
    print("V1", "V2", "Wt")
    ans = 0
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))

    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    rank = [1] * n

    for edge in edges:
        vertex1, vertex2, weight = edge
        flag = union(vertex1, vertex2)

        if not flag:
            print(vertex1, vertex2, weight)
            ans += weight

    return ans
N = int(input("Enter number of vertices: "))
G=[]
print("Enter adjacency matrix:")
for _ in range(N):
    row=list(map(int,input().split()))
    G.append(row)

ans = kruskal_algo(7, G)
print("The min cost is",ans)
