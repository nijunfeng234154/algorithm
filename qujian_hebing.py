
def read_segments():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    segments = [list(map(int, line.split())) for line in data]
    return segments
    
def main():
    # seqs = [[1,2],[2,4],[5,6],[7,8],[7,9]]
    seqs = read_segments()
    seqs.sort()
    my_seq = [-2e9,-2e9]
    res = []
    for i in range(len(seqs)):
        if my_seq[1]<seqs[i][0]:
            if my_seq[0]!=-2e9:
                res.append(my_seq)
            my_seq = seqs[i]
        else:
            my_seq[1] = max(my_seq[1],seqs[i][1])
    if my_seq[0]!=-2e9:
        res.append(my_seq)
    return res

if __name__ == '__main__':
    print(main())        
    
    
    
