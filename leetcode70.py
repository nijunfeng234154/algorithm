def climbStairs(n):
    if n<=2:
        return n
    else:
        return climbStairs(n-1)+climbStairs(n-2)

def main():
    print(climbStairs(3))

main()