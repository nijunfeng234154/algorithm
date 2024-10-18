import math

def judge(x):
    for i in range(0, int(x**(1/3))+1):
        if x - i**3 >=0:
            return True

def main():
    x=0
    if judge(int(x)):
        print('是一个神奇数')
    else:
        print('不是一个神奇数')

if __name__ == '__main__':
    main()