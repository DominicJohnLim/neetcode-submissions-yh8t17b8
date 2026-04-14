class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_s1 = {}
        hash_s2 = {}
        
        for char in s1:
            hash_s1[char] = 1 + hash_s1.get(char, 0)
        
        l = 0
        for r in range(0, len(s2)):
            char = s2[r]
            hash_s2[char] = 1 + hash_s2.get(char, 0)

            # print(hash_s2, hash_s1, char)
            if hash_s2 == hash_s1: return True

            if char not in hash_s1 or hash_s1[char] < hash_s2[char]:
                first = True
                while l < len(s2):
                    if not first:
                        char = s2[l]
                        if l > r or (char in hash_s1 and (hash_s1[char] >= hash_s2[char])):
                            break
                    else:
                        char = s2[l]
                        l += 1
                    
                    hash_s2[char] -= 1
                    if hash_s2[char] <= 0:
                        hash_s2.pop(char)
                    if not first: l += 1
                    first = False
                    # print(l, r, s2[r], char, hash_s2, l < r)

        
        return False
