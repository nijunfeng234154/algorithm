class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(candidates,target,path,start_i):
            if sum(path) == target:
                res.append(path[:])
                return 
            
            for i in range(start_i,len(candidates)):
                if i >start_i and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(candidates,target,path,i+1)
                path.pop()

        dfs(sorted(candidates), target, [] ,0)

        return res

        