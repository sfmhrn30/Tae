def issafe(row,col,board,n):
    duprow=row
    dupcol=col
    while row>=0 and col>=0:
        if board[row][col]=='Q':
            return False
        row-=1
        col-=1
    col=dupcol
    row=duprow
    while col>=0:
        if board[row][col]=='Q':
            return False
        col-=1
    row=duprow
    col=dupcol
    while row<n and col>=0:
        if board[row][col]=='Q':
            return False
        row+=1
        col-=1
    return True
def solve(col,board,ans,n):
    if col==n:
        ans.append(list(board))
        return
    for row in range(n):
        if issafe(row,col,board,n):
            board[row]=board[row][:col]+'Q'+board[row][col+1:]
            solve(col+1,board,ans,n)
            board[row]=board[row][:col]+'*'+board[row][col+1:]
def nqueens(n):
    ans=[]
    board=['*'*n for _ in range(n)]
    solve(0,board,ans,n)
    return ans
n=int(input("Enter no of Queens:"))
ans=nqueens(n)
for row in ans:
    for i in row:
        print(i)
    print()
