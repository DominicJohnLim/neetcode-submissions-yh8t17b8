class Solution:
    def minWindow(self, s: str, t: str) -> str:
        content = {}
        MAX_STRING = "E" * 1001

        for char in t:
            content[char] = 1 + content.get(char, 0)

        output = MAX_STRING
        num_zero = 0
        l = 0
        for r in range(0, len(s)):
            if s[r] in content:
                content[s[r]] -= 1
                if content[s[r]] == 0:
                    num_zero += 1
            
            if num_zero >= len(content):
                while l < len(s):
                    char = s[l]
                    l += 1
                    if char in content:
                        content[char] += 1
                        if content[char] > 0:
                            num_zero -= 1
                            break
                # print(l,r)
                output = min(output, s[l-1:r+1], key=len)
            # collect right until you get a substring
            # move l to prune as much as possible
            # move l to r 
            # break

        return output if output != MAX_STRING else ""
