class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sHash = {}
            for i in range(len(s)):
                sHash[s[i]] = i
            for i in range(len(t)):
                if t[i] not in sHash:
                    return False
            return True
        return False