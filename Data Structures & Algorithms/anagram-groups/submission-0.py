class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        running = []
        global_appear = {}

        for i in range(len(strs)):
            if strs[i] not in global_appear:
                running.append([strs[i]])
                global_appear[strs[i]] = True
                for j in range(i+1, len(strs)):
                    if self.isAnagram(strs[i], strs[j]):
                        running[-1].append(strs[j])
                        global_appear[strs[j]] = True

        return running