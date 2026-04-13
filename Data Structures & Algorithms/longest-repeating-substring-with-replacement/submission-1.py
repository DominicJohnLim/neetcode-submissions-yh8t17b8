class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1: return len(s)

        l = 0
        char_counts = {s[l]: 1}
        output = 0
        for r in range(1, len(s)):
            char_counts[s[r]] = 1 + char_counts.get(s[r], 0)
            max_char = max(char_counts, key = char_counts.get) # chase character            
            other = sum(char_counts.values()) - char_counts[max_char]

            while other > k and l <= r:
                char_counts[s[l]] -= 1
                max_char = max(char_counts, key = char_counts.get) # chase character            
                other = sum(char_counts.values()) - char_counts[max_char]
                l += 1
            
            output = max(output, r - l + 1)

            # print(char_counts)

        return output