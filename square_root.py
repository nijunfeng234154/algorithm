import math

def judge(x):
    sum=0
    for i in range(1, x):
        if x/i == int(x/i):
            sum += i
    if sum == x:
        return True
    return False

def main():
    x=7
    if judge(int(x)):
        print('是一个完全数')
    else:
        print('不是一个完全数')

if __name__ == '__main__':
    main()