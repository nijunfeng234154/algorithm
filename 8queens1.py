col = [0]*100
dg = [0]*100
udg = [0]*100
cnt = 0

def dfs(arr,u,n):
    global cnt
    if u == n:
        # for i in range(n):
        #     for j in range(n):
        #         print(arr[i][j], end=' ')
        # print()
        cnt += 1  
        return
    
    for i in range(n):
        if col[i]==0 and dg[u+i]==0 and udg[n-u+i]==0:
            col[i] = dg[u+i] = udg[n-u+i] = 1
            arr[u][i] = 'Q'
            dfs(arr,u+1,n)
            arr[u][i] = '.'
            col[i] = dg[u+i] = udg[n-u+i] = 0
            


def main():
    global cnt 
    n = 4
    arr = [['.' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = '.'
    
    dfs(arr,0,n)
    print(f"可能的解决方案个数: {cnt}")

main()