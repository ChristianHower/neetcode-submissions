class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            length = len(strs[i])
            encoded += str(length) + "#" + strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        for i in range(len(s)):
            if s[i].isdigit() and s[i+1] == "#":
                length = int(s[i])
                decoded.append(s[i+2:i+length+2])
        return decoded
