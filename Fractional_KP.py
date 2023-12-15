n=int(input("Enter No of Objects:"))
weight=list(map(int,input("Enter Weights:").split()))
profit=list(map(int,input("Enter Profits:").split()))
cap=int(input("Enter Maximum Capacity: "))
total=0
a=[]
for i in range(n):
    a.append([weight[i],profit[i]])
a=sorted(a,key=lambda x:x[1]/x[0],reverse=True)
selected=[]
for i in range(n):
    if a[i][0]<=cap:
        total+=a[i][1]
        selected.append([a[i][0],1])
        cap-=a[i][0]
    else:
        total+=a[i][1]*(cap/a[i][0])
        selected.append([a[i][0],cap/a[i][0]])
        break
print(total)
print(selected)
