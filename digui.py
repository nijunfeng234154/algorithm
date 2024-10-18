def mul(n,m,depth):
    if m == 0 and depth == 0: 
        return 1
    if m == 0 and depth>0:
        return n
    if n == 1:
        return 1
    depth +=1
    return n*mul(n,m-1,depth)

def re_arr(i,j,arr):
    j-=1
    if i>=j: 
        return arr
    else:
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        return re_arr(i+1,j,arr)


if __name__ == '__main__':
    i = -1
    arr = [1,2,3,4,5,6,7]
    j = len(arr)
    # k = int((i+j)/2)
    print(re_arr(i,j,arr))
