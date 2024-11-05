bo = [0]*8
def dfs(res,l,u,result):
    if u == len(l):
        result.append(res[:])
        return 
    
    for i in range(len(l)):
        if bo[l[i]] == 0:
            res.append(l[i])
            bo[l[i]] = 1
            dfs(res, l, u + 1, result)
            bo[l[i]] = 0
            res.pop()
        
        

def main():
    l = [1,2,3]
    print(len(l))
    res = []
    result = []
    dfs(res, l, 0, result)
    for perm in result:
        print(perm)

if __name__ == '__main__':
    main()