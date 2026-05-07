class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(current, last, idx):
            nonlocal res
            if idx > len(s):
                good = True
                for i in current:
                    if i != i[::-1]:
                        good = False
                        break
                if good:
                    res.append(current)
                return

            this = s[last:idx]
            # print(this, current)
            dfs(current + [this], idx, idx + 1)
            if idx + 1 <= len(s): dfs(current, last, idx + 1)
        
        dfs([], 0, 1)
        
        return res