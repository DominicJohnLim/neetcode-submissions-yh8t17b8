class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_string_hash = {}
        second_string_hash = {}

        for char in s:
            if char not in first_string_hash:
                first_string_hash[char] = 1
            else:
                first_string_hash[char] += 1
        
        for char in t:
            if char not in second_string_hash:
                second_string_hash[char] = 1
            else:
                second_string_hash[char] += 1

        for char in first_string_hash:
            if char not in second_string_hash:
                return False
            elif first_string_hash[char] != second_string_hash[char]:
                return False
        
        for char in second_string_hash:
            if char not in first_string_hash:
                return False
            elif first_string_hash[char] != second_string_hash[char]:
                return False

        return True
