class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)

        left = 0
        right = 1
        output = 0
        running = set([s[0]])

        while right < len(s):
            # print(running, s[right], s[left])
            while s[right] in running and left <= right:
                running.remove(s[left])
                left += 1
            running.add(s[right])
            output = max(output, right - left + 1)
            right += 1
        
        return output