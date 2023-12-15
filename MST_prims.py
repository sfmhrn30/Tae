INF = 9999999
N = int(input("Enter number of vertices: "))
G=[]
print("Enter adjacency matrix:")
for _ in range(N):
    row=list(map(int,input().split()))
    G.append(row)
visited = [False]*N
no_edge = 0
visited[0] = True
l=[]
cost=0
row=[]
while (no_edge < N - 1):
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if visited[m]:
            for n in range(N):
                   
                if ((not visited[n]) and G[m][n]):
                    row.append([m+1,n+1,G[m][n]])
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print("List of nodes connected to ",a+1)
    for i in row:
        if i[0]==a+1:
            print(i[1],"-",i[2])
    row=[]
    cost+=G[a][b]
    l.append(str(a+1) + "-" + str(b+1) + ":" + str(G[a][b]))
    print("Minimum edge is ",b+1,"-",G[a][b],"\n")
    visited[b] = True
    no_edge += 1
print("Edge : Weight")
for i in l:
    print(i)
print("Cost of Tree : ",cost)
