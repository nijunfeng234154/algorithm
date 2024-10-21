row = [0]*100
col = [0]*100
dg = [0]*100
udg = [0]*100
cnt = 0

def dfs(x,y,s,n):
    global cnt
    if s>n:
        return 
    
    if y == n:
        y = 0
        x += 1

    if x == n:
        if s == n:
            cnt += 1  
        return
    
    
    #该位置不放皇后的情况
    dfs(x,y+1,s,n)

    #该位置放皇后的情况
    if row[x] == 0 and col[y] == 0 and dg[x+y] == 0 and udg[x-y+n] == 0:
        row[x] = col[y] = dg[x+y] = udg[x-y+n] = 1 
        dfs(x,y+1,s+1,n)
        row[x] = col[y] = dg[x+y] = udg[x-y+n] = 0
    

def main():
    global cnt 
    n = 8

    dfs(0,0,0,n)
    print(f"可能的解决方案个数: {cnt}")    

main()