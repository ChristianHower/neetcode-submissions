class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sHash = {}
            for i in range(len(s)):
                if s[i] not in sHash:
                    count = 1
                    j = i + 1
                    while j < len(s):
                        if s[i] == s[j]:
                            count += 1
                        j += 1
                    sHash[s[i]] = count
            tHash = {}
            for i in range(len(t)):
                if t[i] not in tHash:
                    count = 1
                    j = i + 1
                    while j < len(t):
                        if t[i] == t[j]:
                            count += 1
                        j += 1
                    tHash[t[i]] = count
            if tHash != sHash:
                return False
            return True
        return False