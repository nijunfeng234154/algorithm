import sys

def main():
    n = int(input())
    if n < 0:
        sys.exit()
    print(bin(n)[2:])

main()
print(3//2)