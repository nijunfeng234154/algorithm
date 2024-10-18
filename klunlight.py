def main():
    n,m = input().split(' ')
    n = int(n)
    m = int(m)
    arr = [1 for i in range(n+5)]
    for i in range(1,n+1):
        for j in range(2,m+1):
            if i%j == 0:
                arr[i] = -arr[i]
    for i in range(1,n+1):
        if arr[i] == 1:
            print(i)

if __name__ == '__main__':
    main()