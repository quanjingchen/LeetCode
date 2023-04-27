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
            
            
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(i, target - candidates[i])
                path.pop()
            
        dfs(0, target)       
            
        return paths
                
                
        