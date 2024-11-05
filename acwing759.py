#759 格子染色
def merge_row_col(seqs):
    if not seqs:
        return []
    seqs.sort()
    my_seq = [-2e9,-2e9,0]
    # my_seq = seqs[0]
    res = []
    for i in range(1,len(seqs)):
        if my_seq[1]<seqs[i][0]:
            if my_seq[0]!=-2e9:
                res.append(my_seq)
            my_seq = seqs[i]
        else:
            my_seq[1] = max(my_seq[1],seqs[i][1])
            
    if my_seq[0]!=-2e9:
        res.append(my_seq)
    return res

def ranse_2d():
    n = int(input().strip())
    #处理输入，这里注意写法
    ops = [] 
    for _ in range(n):
        data = input().strip()
        ops.append(list(map(int,data.split())))
    
    row_seqs=[]
    col_seqs=[]

    for op in ops:
        #横排染色
        if op[1] == op[3]:
            row_seqs.append([op[0],op[2],op[1]])
        #纵列染色
        elif op[0] == op[2]:
            col_seqs.append([op[1],op[3],op[2]])
    
    #所有行里已经染色的区间
    row_merged = merge_row_col(row_seqs)
    col_merged = merge_row_col(col_seqs)
    
    #统计
    #使用二维的集合！！记录被染色的格子
    black_cells = set()
    
    for row in row_merged:
        for i in range(row[0], row[1] + 1):
            black_cells.add((i, row[2]))
    
    for col in col_merged:
        for i in range(col[0], col[1] + 1):
            black_cells.add((col[2], i))
    
    # 统计被染色的格子数量
    cnt = len(black_cells)
    print(cnt)            
        
if __name__ == '__main__':
    ranse_2d()
    
    ###目前只能处理正数的情况