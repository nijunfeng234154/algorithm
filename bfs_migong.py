
dx = [0,0,1,-1]
dy = [1,-1,0,0]
d = [[0 for _ in range(m)] for _ in range(n)]
bl = [[0 for _ in range(m)] for _ in range(n)]
path = []
def bfs():
    global m,n
    queue = []
    d[0][0] = 0
    queue[0] = [0,0]
    #在bfs中确保每次搜索只包含最近的点是通过队列实现的
    tt = hh = 0
    while tt <= hh:
        #队头的点
        t = queue[hh]
        hh += 1
        for i in range(len(dx)):
            x = t[0]+dx[i]
            y = t[1]+dy[i]    
            if x<=m-1 and x>=0 and y>=0 and y<=n-1 and bl[x][y]==0 and d[x][y]==-1:
                path.append([x,y])
                queue[tt] = [x,y]
                tt+=1
                d[x][y] = d[t[0]][t[1]]+1
    return d[m-1][n-1]            
                


def main():
    global m,n
    m,n = int(input().strip())
    bfs()


main()