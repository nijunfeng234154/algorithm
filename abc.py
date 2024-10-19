###Ramsey's Algorithm
# There are at least k people in the room, or there are at least k people in the room, and no three of them are mutual friends.
# In discrete mathematics, Ramsey’s theorem states that for any positive integer k, there is an integer m such that in any party with at least m guests, one of the following statements must be true:
# (1) There are at least k guests who know each other.
# (2) There are at least k guests who do not know each other.
# For example, for k = 3, then in any party of at least 6 guests, either there are three guests who know each other, or there are three guests who do not know each other. This question asks you to write a program (using either Python, C, C++ or Java) to help verify Ramsey’s theorem. The input of the program is organized as follows:
# The first line of the input has an integer m, followed by m lines of string, each representing a guest (so there are totally m guests for this input).
# Then, there is another line of integer n, followed by n lines of pair of guests (guest a and guest b know each other if and only if there is a line of pair a, b in the input).
# Then, there is a line containing an integer k.
# For the output, your program should print a set of k guests who knows each other, and if there is no such set, the program should print a set of k guests who do not know each other.
# Following is a sample run of the program.
#4
# a
# b
# c
# d
# 3
# a b
# a c
# b c
# 3
# 0
# 1
# 2
# 0
# 1
# The guests in ['a', 'b', 'c'] know each other
# 4
# a
# b
# c
# d
# 2
# a b
# a c
# 3
# The guests in ['b', 'c', 'd'] do not know each other
# 请写注释

def main():
    m = int(input())
    guests = [input() for _ in range(m)]
    print(guests)
    n = int(input())
    knows = [input().split() for _ in range(n)]
    print(knows)
    k = int(input())

    if k == 0:
        print(guests[:k])
        return

    for i in range(m):
        for j in range(i+1, m):
            for l in range(j+1, m):
                if [guests[i], guests[j], guests[l]] in knows:
                    print(f"The guests in {guests[i], guests[j], guests[l]} know each other")
                    return
    print(f"The guests in {guests[:k]} do not know each other")


if __name__ == '__main__':
    main()