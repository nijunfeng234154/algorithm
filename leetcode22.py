def judge_list(l) -> bool:
    stack = []
    mapping = {')':'('}

    for i in l:
        if i == '(':
            stack.append(i)
        #注意条件
        elif i in mapping and stack and mapping[i] == stack[-1]:
            stack.pop()
        else:
            return False
    
    return not stack

res = []
def dfs(l,n,index):
    if index == 2*n-1:
        if judge_list(l):
            res.append(l[:])
        return 
    
    
    dfs(l.append('('),n,index+1)
    dfs(l.append(')'),n,index+1)


dfs