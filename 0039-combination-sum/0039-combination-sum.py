class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        paths = []
        path = []
        def dfs(index, target):
            if target == 0:
                paths.append(path[:])
            if target <= 0:
                return
            path.append(candidates[index])
            
            for i in range(index, len(candidates)):
                if target - candidates[i] < 0:
                    break
                dfs(i, target - candidates[index])
                
            path.pop()
            
        for i in range(len(candidates)):
            dfs(i, target)       
            
        return paths
                
                
        