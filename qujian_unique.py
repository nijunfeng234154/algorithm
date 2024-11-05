a=[]
def find(x,alls):
    l = 0
    r = len(alls)-1
    while l<r:
        mid = (l+r)>>1
        if alls[mid]>=x:
            r = mid
        else:
            l = mid+1
    return r+1
    
def unique(arr):
    unique_arr = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i - 1]:
            unique_arr.append(arr[i])
    return unique_arr
    
def read_data(n, m):
    adds = []
    querys = []
    for _ in range(n):
        data = input().strip()
        adds.append(list(map(int, data.split())))
    for _ in range(m):
        data = input().strip()
        querys.append(list(map(int, data.split())))
    alls = []
    for query in querys:
        alls.append(query[0])
        alls.append(query[1])
    return adds, alls, querys

def main():
    n, m = map(int, input().strip().split())
    adds, alls, querys = read_data(n, m)
    for add in adds:
        alls.append(add[0])
    alls = sorted(alls)
    
    #去重
    alls = unique(alls)
    
    a = [0]*(len(alls)+5)
    #处理插入
    for add in adds:
        x = find(add[0],alls)
        a[x] += add[1]
        
    #求前缀和
    s=[0]*(len(a))
    for i in range(1,len(a)):
        s[i] = s[i-1]+a[i]
            
    #输出区间和
    for query in querys:
        l = find(query[0], alls)
        r = find(query[1], alls)
        print(s[r]-s[l-1])

if __name__ == '__main__':
    main()
    
    