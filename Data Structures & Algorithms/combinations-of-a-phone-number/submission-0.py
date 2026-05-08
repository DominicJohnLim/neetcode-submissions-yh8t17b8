class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits): return []

        mapping = {
            "2": "ABC",
            "3": "DEF",
            "4": "GHI",
            "5": "JKL",
            "6": "MNO",
            "7": "PQRS",
            "8": "TUV",
            "9": "WXYZ"
        }

        output = []

        def dfs(current, idx):
            nonlocal output
            if idx == len(digits):
                output.append(current.lower())
                return
            
            for i in mapping[digits[idx]]:
                dfs(current + i, idx + 1)
            
        dfs("", 0)

        return output